from app_blog import db
import datetime as dt


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow,
                           onupdate=dt.datetime.utcnow)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Tag id={self.id} name={self.name}>"


tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tags.id', primary_key=True)),
                db.Column('article_id', db.Integer, db.ForeignKey('tags.id', primary_key=True))
                )
