from app.form import HumanVoteForm
from app.model import HumanVote


class HumanVoteService:
    @staticmethod
    def create(form: HumanVoteForm) -> HumanVote:
        vote = HumanVote()
        form.populate_obj(vote)
        HumanVote.save(vote)
        return vote

    @staticmethod
    def get_all() -> tuple[list[HumanVote], int]:
        votes = HumanVote.find_all()
        current_group = len(votes) + 1
        return votes, current_group

    @staticmethod
    def get_first() -> HumanVote | None:
        return HumanVote.find_first()

    @classmethod
    def delete_all(cls) -> None:
        votes, _ = cls.get_all()
        for vote in votes:
            HumanVote.delete(vote)
