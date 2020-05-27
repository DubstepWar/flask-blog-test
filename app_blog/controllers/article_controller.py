from typing import List

from flask import Blueprint, jsonify, request

from app_blog.extensions import db
from app_blog.models import Article

articles_blueprint = Blueprint("articles", __name__, url_prefix="/articles")


@articles_blueprint.route("", methods=["GET"])
def get_articles():
    articles: List[Article] = Article.query.all()

    result = [article.to_dict() for article in articles]
    return jsonify({
        "result": result,
        "status": "ok",
        "success": True
    })


@articles_blueprint.route("/create", methods=["POST"])
def create_article():
    data = request.get_json()

    article = Article(**data)

    db.session.add(article)
    db.session.commit()

    return jsonify({
        "result": article.to_dict(),
        "status": "ok",
        "success": True
    }), 201


@articles_blueprint.route("/<int:article_id>")
def get_article(article_id):
    article: Article = Article.query.get_or_404(article_id)

    return jsonify({
        "success": True,
        "status": "Ok",
        "result": article.to_dict()
    })
