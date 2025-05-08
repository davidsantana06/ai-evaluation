from dotenv import load_dotenv
from flask import Flask, redirect

from app.extension import db
from app.facade import Flash, Template, Url
from app.model import *

from .parameter import Parameter
from .path import Path


class Setup:
    @staticmethod
    def apply_parameters(app: Flask) -> None:
        load_dotenv(Path.ENV_FILE)
        app.config.from_object(Parameter)
        app.static_folder = Path.STATIC_FOLDER
        app.template_folder = Path.TEMPLATE_FOLDER

    @staticmethod
    def initialize_db(app: Flask) -> None:
        db.init_app(app)
        with app.app_context():
            db.create_all()

    @staticmethod
    def register_views(app: Flask) -> None:
        ...

    @staticmethod
    def _handle_error(_: Exception):
        Flash.append("danger", "Ops! Algo deu errado")
        return redirect(Url.for_view("home:index"))

    @classmethod
    def register_error_handler(cls, app: Flask) -> None:
        app.register_error_handler(Exception, cls._handle_error)

    @staticmethod
    def inject_jinja_globals(app: Flask) -> None:
        app.context_processor(
            lambda: {
                "layout": (lambda layout: Template.resolve(f"layout/{layout}")),
                "macro": (lambda macro: Template.resolve(f"macro/{macro}")),
                "partial": (lambda partial: Template.resolve(f"partial/{partial}")),
                "static": Url.for_static,
                "view": Url.for_view,
                "flashes": Flash.pop_all(),
            }
        )
