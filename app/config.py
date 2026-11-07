import os
from dotenv import load_dotenv

# Read the values from the .env file into environment variables
load_dotenv()


class Config:
    # The secret key signs the session cookie.
    # It comes from .env so it is never written in the code or uploaded to GitHub.
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Debug is OFF unless FLASK_DEBUG=1 is set (secure default)
    DEBUG = os.environ.get("FLASK_DEBUG") == "1"
