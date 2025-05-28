from os import environ
from .path import Path


class Parameter:
    SECRET_KEY = environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path.DATABASE_FILE}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False

    GEMINI_AI_KEY = environ.get("GEMINI_AI_KEY")

    OPEN_AI_KEY = environ.get("OPEN_AI_KEY")

    RUNWARE_AI_KEY = environ.get("RUNWARE_AI_KEY")

    STABILITY_AI_KEY = environ.get("STABILITY_AI_KEY")
