from flask import Flask
from .config import Config
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    if not app.config["SECRET_KEY"] or app.config["SECRET_KEY"] == "change-me":
        raise RuntimeError("SECRET_KEY is missing. Copy .env.example to .env and set a real key.")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .routes import main
    app.register_blueprint(main)

    return app
