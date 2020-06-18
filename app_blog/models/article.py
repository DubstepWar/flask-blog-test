import datetime as dt
from app_blog.extensions import db, ma

from .category import Category
from .tag import Tag

from app_blog.models.tag import article_tags


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(110), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id", ondelete="CASCADE"), nullable=True
    )
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow
    )

    category = db.relationship(
        Category, backref=db.backref("articles", lazy=True), lazy=False
    )

    tags = db.relationship(
        Tag,
        secondary=article_tags,
        lazy="subquery",
        backref=db.backref("articles", lazy=True),
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Article id={self.id} title={self.title}>"


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        include_fk = True  # включает в JSON внешние ключи

    slug = ma.auto_field(dump_only=True)
    created_at = ma.auto_field(dump_only=True)
    updated_at = ma.auto_field(dump_only=True)


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
