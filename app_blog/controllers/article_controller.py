from flask import Blueprint, jsonify, request
from typing import List

from app_blog.extensions import db
from app_blog.models import Article
from app_blog.models.article import article_schema
from app_blog.services.article_service import ArticleService

articles_blueprint = Blueprint("articles", __name__, url_prefix="/articles")


@articles_blueprint.route("", methods=["GET", "POST"])
def get_articles():
    if request.method == "GET":
        articles: List[Article] = ArticleService.get_articles()

        return jsonify({
            "result": articles,
            "status": "ok",
            "success": True
        })
    elif request.method == "POST":
        article: Article = ArticleService.create_article(request)

        db.session.add(article)
        db.session.commit()

        article_dict = article_schema.dump(article)

        return jsonify({
            "result": article_dict,
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
