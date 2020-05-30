from typing import List

from app_blog.models import Article
from app_blog.models.article import ArticleSchema


class ArticleService:

    def __init__(self):
        pass

    @staticmethod
    def get_articles():
        articles: List[Article] = Article.query.all()
        print(articles)

        return articles

    @staticmethod
    def create_article(request):
        data = request.get_json()
        article = Article(**data)

        return article

