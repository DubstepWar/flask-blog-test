from flask import Flask
from flask_cors import CORS

from app_blog.models.user import User
from config import Configuration

from .controllers import register_blueprints
from .extensions import db, migrate, ma, jwt


app = Flask(__name__)
app.config.from_object(Configuration)
# flask cors
CORS(app)

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app, User.authenticate, User.identity)

# register controllers/blueprints
register_blueprints(app)
