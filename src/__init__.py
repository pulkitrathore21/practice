from flask import Flask
import logging

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2://admin:1234@localhost:5432/my_practice"
    logging.basicConfig(
        filename="app.log",
        filemode="w",
        format="%(name)s - %(levelname)s - %(message)s",
    )
    from src import views
    app.register_blueprint(views.user_api)
    
    db.init_app(app)
    migrate = Migrate(app, db)
    from src.models import User
    

    return app
