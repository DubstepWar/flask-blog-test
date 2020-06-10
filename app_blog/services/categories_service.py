from typing import List, Optional
from flask import Request

from app_blog.models.category import Category, categories_schema


class CategoriesService:

    def __init__(self):
        self.categories: List[Category] = []
        self.category: Optional[Category] = None

    def get_categories(self):
        self.categories = Category.qury.all()
        return categories_schema.dump(self.categories)

    def add_category(self, request: Request):
        data = request.get_json()
        self.category = Category(**data)

        return self.category

    def update_category(self, category: Category, request: Request):
        data = request.get_json()
        category.name = data['name']
        self.category = category

        return self.category


categories_service = CategoriesService()
