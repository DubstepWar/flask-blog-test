from flask import Blueprint, jsonify, request

from app_blog.extensions import db, v
from app_blog.models import Article
from app_blog.models.article import article_schema
from app_blog.services.article_service import article_service
from app_blog.validation_rules.article_rules import create_article_rules

articles_blueprint = Blueprint("articles", __name__, url_prefix="/articles")


@articles_blueprint.route("", methods=["GET", "POST"])
def get_articles():
    if request.method == "GET":
        articles = article_service.get_articles()

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

        article: Article = article_service.create_article(request)

        db.session.add(article)
        db.session.commit()

        return jsonify({
            "status": "ok",
            "success": True
        }), 201


@articles_blueprint.route("/<string:article_slug>", methods=['GET', 'PUT', 'DELETE'])
def get_article(article_slug):
    article = Article.query.filter_by(slug=article_slug).first()
    print(article_slug)
    print(article)
    if not article:
        return jsonify({
            "status": "error",
            "errors": ['Not found'],
            "success": False
        })

    if request.method == 'GET':
        return jsonify({
            "success": True,
            "status": "Ok",
            "result": article_schema.dump(article)
        })

    if request.method == 'PUT':
        if not v.validate(request.get_json(), create_article_rules):
            return jsonify({
                "status": "error",
                "errors": v.errors,
                "success": False
            })
        article_service.update_article(article, request)
        db.session.commit()

        return jsonify({
            "success": True,
            "status": "Ok",
        })

    if request.method == 'DELETE':
        db.session.delete(article)
        db.session.commit()

        return jsonify({
            "success": True,
            "status": "Ok",
        })
