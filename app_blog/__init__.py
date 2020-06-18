from flask import Flask
from flask_cors import CORS

from config import Configuration

from .controllers import register_blueprints
from .auth import jwt
from .extensions import db, migrate, ma


app = Flask(__name__)
app.config.from_object(Configuration)
# flask cors
CORS(app)

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

# register controllers/blueprints
register_blueprints(app)
