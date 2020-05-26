from flask import Flask
from flask_migrate import Migrate, Manager, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from config import Configuration
from .controllers import register_blueprints

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

# register controllers/blueprints
register_blueprints(app)

if __name__ == "__main__":
    manager.run()
