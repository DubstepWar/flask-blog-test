from flask import Flask

from app_blog.controllers.auth_controller import auth_blueprint
from app_blog.controllers.categories_controller import categories_blueprint
from app_blog.controllers.users_controller import users_blueprint
from .article_controller import articles_blueprint
from .index_controller import index_blueprint


def register_blueprints(app: Flask):
    app.register_blueprint(index_blueprint)
    app.register_blueprint(articles_blueprint)
    app.register_blueprint(categories_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(users_blueprint)
