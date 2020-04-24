from flask import Flask

from app_blog.database.db import db_session, init_db
from config import Configuration
from .controllers import register_blueprints

app = Flask(__name__)
app.config.from_object(Configuration)

init_db()

register_blueprints(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
