from app_blog import db
import datetime as dt


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=dt.datetime.utcnow,
                           onupdate=dt.datetime.utcnow)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category id={self.id} name={self.name}>"
