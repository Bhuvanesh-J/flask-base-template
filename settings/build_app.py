from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from common.middleware import middleware
from settings.config.database import connect_to_db
from .views import global_errorhandler, homepage

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app = connect_to_db(app)
    homepage(app)
    middleware(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    global_errorhandler(app)
    return app
