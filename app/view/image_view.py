from flask_classful import FlaskView
from app.service import ImageService
from .mixin import ResponseMixin


class ImageView(FlaskView, ResponseMixin):
    def index(self):
        # ai_votes = AiVoteService.get_all()
        # human_votes = HumanVoteService.get_all()
        # has_voted_all = len(ai_votes) == len(human_votes)
        has_voted_all = True
        if not has_voted_all:
            return self._redirect_to("human_vote:index")
        # images = ImageService.get_all()
        images = [
            {
                "group": 1,
                "id": 1,
                "ai": "DALL-E 3",
                "filename": "image-template.png",
                "ai_vote": True,
                "human_vote": False,
            },
            {
                "group": 1,
                "id": 2,
                "ai": "Midjourney",
                "filename": "image-template.png",
                "ai_vote": False,
                "human_vote": False,
            },
            {
                "group": 1,
                "id": 3,
                "ai": "Stable Diffusion",
                "filename": "image-template.png",
                "ai_vote": False,
                "human_vote": False,
            },
            {
                "group": 2,
                "id": 4,
                "ai": "Leonardo AI",
                "filename": "image-template.png",
                "ai_vote": False,
                "human_vote": False,
            },
            {
                "group": 2,
                "id": 5,
                "ai": "Canva AI",
                "filename": "image-template.png",
                "ai_vote": False,
                "human_vote": False,
            },
            {
                "group": 2,
                "id": 6,
                "ai": "Adobe Firefly",
                "filename": "image-template.png",
                "ai_vote": True,
                "human_vote": True,
            },
        ]
        return self._render_page("image/index", images=images)
