from flask_classful import FlaskView
from .mixin import ResponseMixin


class HomeView(FlaskView, ResponseMixin):
    route_base = "/"

    def index(self):
        return self._render_page("home/index")
