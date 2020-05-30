from flask import Flask

from config import Configuration

from .controllers import register_blueprints
from .extensions import db, migrate, ma

app = Flask(__name__)
app.config.from_object(Configuration)

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)

# register controllers/blueprints
register_blueprints(app)
