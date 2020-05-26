from typing import List

from flask import Blueprint, jsonify, request, abort

from app_blog import db
from app_blog.models.article import Article

articles_blueprint = Blueprint("articles", __name__, url_prefix="/articles")


@articles_blueprint.route("/", methods=["GET"])
def get_articles():
    articles: List[Article] = Article.query.all()

    return jsonify(articles)


@articles_blueprint.route("/create", methods=["POST"])
def create_article():
    response = request.data.decode()
    print(response)

    if not response:
        abort(404)

    article = Article(title="title test", slug="slug", description="desc")

    db.session.add(article)
    db.session.commit()

    return "ok"
