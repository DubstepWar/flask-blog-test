from app import app
from flask import request

from app.database.db import db
from app.models.article import Article, article_schema


@app.route('/')
def home():
    return '<h1>Home page</>'


@app.route('/article', methods=['POST'])
def add_article():
    title = request.json['title']
    description = request.json['description']

    new_article = Article(title, description)

    db.session.add(new_article)
    db.session.commit()
    return article_schema.jsonify(new_article)
