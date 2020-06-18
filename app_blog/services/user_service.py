from typing import Optional, List

from app_blog.models.user import User, users_schema


class UserService:
    def __init__(self):
        self.users: List[User] = []
        self.user: Optional[User] = None

    def get_user(self, user_id: int):
        return User.query.get_or_404(user_id)

    def get_user_by_username(self, username: str) -> User:
        return User.query.filter_by(username=username).first_or_404()

    def get_users(self):
        self.users = User.query.all()
        return users_schema.dump(self.users)


user_service = UserService()
