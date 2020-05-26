from sqlalchemy import Column, Integer, String

from app_blog import db


class Article(db.Model):

    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(110))
    slug = Column(String(200), unique=True)
    description = Column(String(200))

    def __init__(self, title=None, description=None, slug=None):
        self.title = title
        self.slug = slug
        self.description = description

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Article title={self.title}>"
