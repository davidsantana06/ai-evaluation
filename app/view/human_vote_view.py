from flask import request
from flask_classful import FlaskView

from app.facade import Flash
from app.form import HumanVoteForm
from app.service import HumanVoteService, ImageService

from .mixin import ResponseMixin


class HumanVoteView(FlaskView, ResponseMixin):
    def index(self):
        _, current_group = HumanVoteService.get_all()
        images = ImageService.get_all_by_group(current_group)

        is_voting = len(images) > 0
        if not is_voting:
            return self._redirect_to("image:index")

        return self._render_page("human_vote/index", images=images)

    def post(self):
        _, current_group = HumanVoteService.get_all()
        image = ImageService.get_one_by_group(current_group)

        is_voting = image is not None
        if not is_voting:
            Flash.append("success", "Você avaliou todas as imagens")
            return self._redirect_to("image:index")

        form = HumanVoteForm(request.form)
        HumanVoteService.create(form)
        return self._redirect_to("human_vote:index")

    def reset(self):
        next = request.args.get("next", "home:index")
        vote = HumanVoteService.get_first()

        has_voted_one = vote is not None
        if has_voted_one:
            HumanVoteService.delete_all()
            Flash.append("info", "Seu progresso foi reiniciado")

        return self._redirect_to(next)
