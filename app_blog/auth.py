from flask_jwt import JWT
from werkzeug.security import safe_str_cmp

from .services.user_service import user_service


# Используя декораторы
jwt = JWT()


@jwt.authentication_handler
def authenticate(username, password):
    user = user_service.get_user_by_username(username)
    if user and safe_str_cmp(user.password.encode("utf-8"), password.encode("utf-8")):
        return user


@jwt.identity_handler
def identity(payload):
    user_id = int(payload["identity"])
    return user_service.get_user(user_id)


# или так, без декораторов
# jwt = JWT(authentication_handler=authenticate, identity_handler=identity)
