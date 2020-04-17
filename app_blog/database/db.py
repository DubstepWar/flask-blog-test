from app_blog import app
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)
ma = Marshmallow(app)
