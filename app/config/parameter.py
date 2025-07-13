from os import environ
from .path import Path


class Parameter:
    SECRET_KEY = environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path.DATABASE_FILE}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False

    JSON_SORT_KEYS = False

    GEMINI_KEY = environ.get("GEMINI_KEY")

    OPENAI_KEY = environ.get("OPENAI_KEY")

    RUNWARE_KEY = environ.get("RUNWARE_KEY")

    STABILITY_AI_KEY = environ.get("STABILITY_AI_KEY")
