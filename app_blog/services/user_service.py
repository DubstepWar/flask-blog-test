from typing import Optional, List

from app_blog.models.user import User, users_schema


class UserService:

    def __init__(self):
        self.users: List[User] = []
        self.user: Optional[User] = None
        self.usernames_list: List[str] = []
        self.user_ids_list: List[int] = []

    def get_users(self):
        self.users = User.query.all()
        return users_schema.dump(self.users)

    def get_usernames_list(self):
        self.usernames_list = User.query.with_entries(User.username)

        return self.usernames_list

    def get_user_ids_list(self):
        self.user_ids_list = User.query.with_entries(User.id)

        return self.user_ids_list


user_service = UserService()
