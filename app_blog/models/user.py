from werkzeug.security import safe_str_cmp

from app_blog.extensions import db, ma
from app_blog.services.user_service import user_service


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'User email={self.email} username={self.username}'

    @staticmethod
    def authenticate(username, password):
        usernames_list = user_service.get_usernames_list()
        user = usernames_list.get(username, None)
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user_ids_list = user_service.get_user_ids_list()
        return user_ids_list.get(user_id, None)


class UserSchema(ma.SQLAlchemyAutoSchema):
    model = User
    # include_fk = True хз что это


user_schema = UserSchema()
users_schema = UserSchema(many=True)
