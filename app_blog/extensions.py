from cerberus import Validator
from flask_jwt import JWT
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
v = Validator()
jwt = JWT()
