from typing import List, Optional

from slugify import slugify

from app_blog.extensions import db
from app_blog.models import Article
from app_blog.models.category import Category


class ArticleService:
    def __init__(self):
        self.articles: List[Article] = []
        self.article: Optional[Article] = None

    # не работает вроде
    def get_articles(self):
        return Article.query\
            .join(Category, Article.category_id == Category.id)\
            .all()

    def create_article(self, data) -> Article:
        data["slug"] = slugify(data["title"])

        article = Article(**data)

        db.session.add(article)
        db.session.commit()

        return article

    def update_article(self, article: Article, data) -> Article:
        article.title = data["title"]
        article.content = data["content"]
        # еще категория, и все остальное, что нужно для обновления

        db.session.add(article)
        db.session.commit()

        return article


article_service = ArticleService()
