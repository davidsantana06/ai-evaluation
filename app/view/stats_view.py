from flask_classful import FlaskView
from app.service import StatsService


class StatsView(FlaskView):
    def index(self):
        return StatsService.summarize()
