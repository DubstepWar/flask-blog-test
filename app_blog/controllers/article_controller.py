from flask import request

from ..database.db import db
from ..models.article import Article, article_schema


def add_article():
    title = request.json["title"]
    description = request.json["description"]

    new_article = Article(title, description)

    db.session.add(new_article)
    db.session.commit()

    return article_schema.jsonify(new_article)
