from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)
ma = Marshmallow(app)
