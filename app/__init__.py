from flask import Flask
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Fail securely: stop the app if there is no proper secret key
    if not app.config["SECRET_KEY"] or app.config["SECRET_KEY"] == "change-me":
        raise RuntimeError("SECRET_KEY is missing. Copy .env.example to .env and set a real key.")

    # Register the pages (routes)
    from .routes import main
    app.register_blueprint(main)

    return app
