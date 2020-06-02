from typing import List

from app_blog.models import Article
from app_blog.models.article import articles_schema, article_schema


class ArticleService:

    def __init__(self):
        pass

    @staticmethod
    def get_articles():
        articles: List[Article] = Article.query.all()

        return articles_schema.dump(articles)

    @staticmethod
    def create_article(request):
        data = request.get_json()
        print(data)
        article = Article(**data)

        return article

