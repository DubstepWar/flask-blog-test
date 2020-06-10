from flask import Blueprint, request, jsonify

from app_blog.extensions import v, db
from app_blog.models.category import Category, category_schema
from app_blog.services.categories_service import categories_service
from app_blog.validation_rules.category_rules import create_category_rules

categories_blueprint = Blueprint("categories", __name__, url_prefix="/categories")


@categories_blueprint.route("", methods=["GET", "POST"])
def get_categories():
    if request.method == 'GET':
        categories = categories_service.get_categories()

        return jsonify({
            "result": categories,
            "status": "ok",
            "success": True
        })
    if request.method == 'POST':
        if not v.validate(request.get_json(), create_category_rules):
            return jsonify({
                "status": "error",
                "errors": v.errors,
                "success": False
            })
        category = categories_service.add_category(request)
        db.session.add(category)
        db.commit()

        return jsonify({
            "status": "ok",
            "success": True
        }), 201


@categories_blueprint.route("/<int:category_id>", methods=['GET', 'PUT', 'DELETE'])
def get_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({
            "status": "error",
            "errors": ['Not found'],
            "success": False
        })
    if request.method == 'GET':
        return jsonify({
            "success": True,
            "status": "Ok",
            "result": category_schema.dump(category)
        })

    if request.method == 'PUT':
        if not v.validate(request.get_json(), create_category_rules):
            return jsonify({
                "status": "error",
                "errors": v.errors,
                "success": False
            })
        categories_service.update_category(category, request)
        db.session.commit()

        return jsonify({
            "success": True,
            "status": "Ok",
        })

    if request.method == 'DELETE':
        db.session.delete(category)
        db.session.commit()

        return jsonify({
            "success": True,
            "status": "Ok",
        })

