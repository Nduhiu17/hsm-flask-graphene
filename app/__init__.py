from os import environ

from flask import Flask
from flask_cors import CORS

from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()



def handle_unauthorized(error):
    return {"status": 401, "title": "Unauthorized", "message": "admin role required"}, 401


def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.debug = True
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
    CORS(app)
    app.config.from_object('config.Config')
    app.config['SQLALCHEMY_ECHO'] = True

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)



    with app.app_context():
        from app.models.user_model import User

        # Register Blueprints

        # will break the build if cannot connect to the db
        db.create_all()
        return app
