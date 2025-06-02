from dotenv import load_dotenv
from flask import Flask, redirect

from app.extension import db
from app.facade import Flash, Template, Url
from app.model import *
from app.service import AiVoteService, ImageService, OpenAiService, SetupService
from app.view import HomeView, HumanVoteView, ImageView, StatsView

from .parameter import Parameter
from .path import Path


class Setup:
    @staticmethod
    def apply_parameters(app: Flask) -> None:
        load_dotenv(Path.ENV_FILE)
        app.config.from_object(Parameter)
        app.json.sort_keys = Parameter.JSON_SORT_KEYS
        app.static_folder = Path.STATIC_FOLDER
        app.template_folder = Path.TEMPLATE_FOLDER

    @staticmethod
    def initialize_db(app: Flask) -> None:
        db.init_app(app)
        with app.app_context():
            db.create_all()

    @staticmethod
    def register_views(app: Flask) -> None:
        HomeView.register(app)
        HumanVoteView.register(app)
        ImageView.register(app)
        StatsView.register(app)

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

    @staticmethod
    def generate_images(app: Flask) -> None:
        generation_entries = SetupService.get_generation_entries()

        with app.app_context():
            images = ImageService.get_all()

            has_generated_one = len(images) > 0
            if has_generated_one:
                return

            for entry in generation_entries:
                ais = SetupService.randomize_ais()
                for ai in ais:
                    SetupService.create_image(ai, **entry)

    @staticmethod
    def evaluate_images(app: Flask) -> None:
        generation_entries = SetupService.get_generation_entries()
        with app.app_context():
            vote = AiVoteService.get_first()

            has_generated_one = vote is not None
            if has_generated_one:
                return

            for entry in generation_entries:
                group = entry["group"]
                images = ImageService.get_all_by_group(group)
                voted_id = OpenAiService.evaluate_images(images)
                AiVoteService.create(voted_id)

    @staticmethod
    def _handle_error(_: Exception):
        Flash.append("danger", "Ops! Algo deu errado")
        return redirect(Url.for_view("home:index"))

    @classmethod
    def register_error_handler(cls, app: Flask) -> None:
        app.register_error_handler(Exception, cls._handle_error)
