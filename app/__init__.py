from flask import Flask
from .database import init_db
from .routes import configure_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SECRET_KEY'] = '123456'
    init_db(app)
    configure_routes(app)

    return app