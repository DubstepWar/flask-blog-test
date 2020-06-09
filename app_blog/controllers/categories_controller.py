from flask import Blueprint

categories_blueprint = Blueprint("categories", __name__, url_prefix="/categories")


@categories_blueprint.route("", methods=["GET", "POST"])
def get_categories():
    return '123'
