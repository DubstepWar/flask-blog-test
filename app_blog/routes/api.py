from app_blog import app
from app_blog.controllers import article_controller, index_controller

app.add_url_rule("/", "index", index_controller.index)
app.add_url_rule(
    "/article", "article", article_controller.add_article, methods=["POST"]
)
