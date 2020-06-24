from flask import Blueprint, jsonify

from app_blog.services.users_service import users_service

users_blueprint = Blueprint("users", __name__, url_prefix="/users")


@users_blueprint.route('/info/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    user = users_service.get_user(user_id)
    return jsonify(user)
