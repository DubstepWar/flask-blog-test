from flask import Blueprint, request, jsonify, make_response

from app_blog.extensions import db
from app_blog.models.user import User

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/register", methods=["POST"])
def register():
    # get the post data
    post_data = request.get_json()

    # check if user already exists
    user = User.query.filter_by(email=post_data.get("email")).first()
    if user:
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return jsonify(response_object), 403

    try:
        user = User(
            email=post_data.get("email"),
            password=post_data.get("password"),
            username=post_data.get("username"),
        )

        # insert the user
        db.session.add(user)
        db.session.commit()

        response_object = {
            "status": "success",
            "message": "Successfully registered.",
        }

        return jsonify(response_object), 201
    except Exception:
        response_object = {
            "status": "fail",
            "message": "Some error occurred. Please try again.",
        }
        return jsonify(response_object), 401
