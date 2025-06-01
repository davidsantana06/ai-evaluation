from flask_classful import FlaskView
from app.service import AiVoteService, HumanVoteService, ImageService
from .mixin import ResponseMixin


class ImageView(FlaskView, ResponseMixin):
    def index(self):
        ai_votes = AiVoteService.get_all()
        human_votes, _ = HumanVoteService.get_all()

        has_voted_all = len(ai_votes) == len(human_votes)
        if not has_voted_all:
            return self._redirect_to("human_vote:index")

        images = ImageService.get_all()
        return self._render_page("image/index", images=images)
