from sqlalchemy import Column, Integer, String
from ..database.db import Base


class Article(Base):

    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    description = Column(String(200))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return "<Article %r>" % self.title
