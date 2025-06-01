from flask import Flask
from .config import Setup


app = Flask(__name__)

Setup.apply_parameters(app)
Setup.initialize_db(app)
Setup.register_views(app)
Setup.inject_jinja_globals(app)
Setup.register_error_handler(app)
Setup.generate_images(app)
Setup.evaluate_images(app)
