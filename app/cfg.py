import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'db.sqlite')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
