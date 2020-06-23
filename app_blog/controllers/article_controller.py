from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required
from marshmallow import ValidationError

from app_blog.extensions import db
from app_blog.models import Article
from app_blog.models.article import article_schema, articles_schema
from app_blog.services.article_service import article_service

articles_blueprint = Blueprint("articles", __name__, url_prefix="/articles")


@articles_blueprint.route("", methods=["GET"])
def get_articles():
    articles = article_service.get_articles()

    return jsonify(articles_schema.dump(articles))


@articles_blueprint.route("", methods=["POST"])
@jwt_required()
def create_article():
    data = request.get_json()

    if not data:
        return (
            {"status": "error", "success": False, "message": "No input data provided"},
            400,
        )

    # Валидируем входящие данные
    try:
        data = article_schema.load(data)
    except ValidationError as err:
        return err.messages, 422
        return (
            jsonify({"status": "error", "errors": err.messages, "success": False}),
            422,
        )

    article = article_service.create_article(data)

    return (
        jsonify(
            {"status": "ok", "success": True, "result": article_schema.dump(article)}
        ),
        201,
    )


@articles_blueprint.route("/<slug>", methods=["GET"])
def get_article(slug):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        return jsonify({"status": "error", "message": "Not found", "success": False})

    return jsonify(article_schema.dump(article))


@articles_blueprint.route("/<slug>", methods=["PUT"])
@jwt_required()
def update_article(slug):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        return jsonify({"status": "error", "message": "Not found", "success": False})

    data = request.get_json()

    if not data:
        return (
            {"status": "error", "success": False, "message": "No input data provided"},
            400,
        )

    # Валидируем входящие данные
    try:
        data = article_schema.load(data)
    except ValidationError as err:
        return err.messages, 422
        return (
            jsonify({"status": "error", "errors": err.messages, "success": False}),
            422,
        )

    article_service.update_article(article, data)

    return jsonify(
        {"success": True, "status": "Ok", "result": article_schema.dump(article)}
    )


@articles_blueprint.route("/<slug>", methods=["DELETE"])
@jwt_required()
def delete_article(slug):
    article = Article.query.filter_by(slug=slug).first()
    if not article:
        return jsonify({"status": "error", "message": "Not found", "success": False})

    db.session.delete(article)
    db.session.commit()

    return jsonify({"success": True, "status": "Ok"})
