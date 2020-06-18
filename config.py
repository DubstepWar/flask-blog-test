import datetime as dt
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'blog-db.sqlite')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_AUTH_URL_RULE = "/auth/login"
    JWT_EXPIRATION_DELTA = dt.timedelta(
        days=7
    )  # Ставим здесь желаемое время действия токена
