from typing import Dict

create_article_rules: Dict = {
    "title": {"type": "string", "required": True},
    "slug": {"type": "string"},
    "content": {"type": "string"},
}
