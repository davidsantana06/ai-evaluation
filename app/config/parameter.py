from os import environ
from .path import Path


class Parameter:
    SECRET_KEY = environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path.DATABASE_FILE}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False
