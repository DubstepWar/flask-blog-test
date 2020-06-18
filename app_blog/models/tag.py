import datetime as dt
from app_blog.extensions import db, ma


class Tag(db.Model):
    __tablename__ = "tags"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Tag id={self.id} name={self.name}>"


class TagSchema(ma.SQLAlchemyAutoSchema):
    model = Tag
    # include_fk = True хз что это


tag_schema = TagSchema()
tags_schema = TagSchema(many=True)

article_tags = db.Table(
    "article_tags",
    db.Column("article_id", db.Integer, db.ForeignKey("articles.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), primary_key=True),
)
