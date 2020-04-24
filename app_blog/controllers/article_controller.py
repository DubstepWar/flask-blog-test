from flask import Blueprint, jsonify
from ..models.article import Article

articles_blueprint = Blueprint("articles", __name__, url_prefix="/articles")


@articles_blueprint.route("/")
def get_articles():
    articles = Article.query.all()
    print(articles)

    return jsonify(articles)
