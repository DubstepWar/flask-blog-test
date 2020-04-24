from flask import Flask

from app_blog.controllers.article_controller import articles_blueprint
from app_blog.controllers.index_controller import index_blueprint


def register_blueprints(app: Flask):
    app.register_blueprint(index_blueprint)
    app.register_blueprint(articles_blueprint)
