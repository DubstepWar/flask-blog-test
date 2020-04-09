from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from cfg import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, title, description):
        self.title = title
        self.description = description


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


@app.route('/article', methods=['POST'])
def add_article():
    title = request.json['title']
    description = request.json['description']

    new_article = Article(title, description)

    db.session.add(new_article)
    db.session.commit()
    return article_schema.jsonify(new_article)


if __name__ == '__main__':
    app.run()
