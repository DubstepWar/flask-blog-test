from typing import List, Optional

from slugify import slugify

from app_blog.models import Article
from app_blog.models.article import articles_schema


class ArticleService:

    def __init__(self):
        self.articles: List[Article] = []
        self.article: Optional[Article] = None

    def get_articles(self):
        self.articles = Article.query.all()

        return articles_schema.dump(self.articles)

    def create_article(self, request):
        data = request.get_json()
        data['slug'] = slugify(data['title'])
        self.article = Article(**data)

        return self.article


article_service = ArticleService()

