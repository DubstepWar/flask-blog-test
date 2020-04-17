from app_blog.database.db import db
from app_blog.database.db import ma


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, title, description):
        self.title = title
        self.description = description


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description")


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
