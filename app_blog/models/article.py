from app_blog.extensions import db, ma
import datetime as dt
from .tag import tags


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(110), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow,
                           onupdate=dt.datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=True)
    category = db.relationship('Category',
                               backref=db.backref('articles', lazy=True))

    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('articles', lazy=True))

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Article id={self.id} title={self.title}>"


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        # include_fk = True хз что это


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
