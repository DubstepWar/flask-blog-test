from flask import Blueprint, jsonify, request
from typing import List

from app_blog.extensions import db, v
from app_blog.models import Article
from app_blog.models.article import article_schema
from app_blog.services.article_service import ArticleService
from app_blog.validation_rules.article_rules import create_article_rules

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
        if not v.validate(request.get_json(), create_article_rules):
            return jsonify({
                "status": "error",
                "errors": v.errors,
                "success": False
            })

        article: Article = ArticleService.create_article(request)

        db.session.add(article)
        db.session.commit()

        return jsonify({
            "result": article_schema.dump(article),
            "status": "ok",
            "success": True
        }), 201

    @articles_blueprint.route("/<string:article_slug>")
    def get_article(article_slug):
        article: Article = Article.query.get_or_404(article_slug)

        return jsonify({
            "success": True,
            "status": "Ok",
            "result": article.to_dict()
        })
