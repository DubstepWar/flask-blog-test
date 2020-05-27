from sqlalchemy import Column, Integer, String, Text

from app_blog.extensions import db


class Article(db.Model):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(110), nullable=False)
    slug = Column(String(200), unique=True)
    content = Column(Text, nullable=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Article id={self.id} title={self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "content": self.content
        }
