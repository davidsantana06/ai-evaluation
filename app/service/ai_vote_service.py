from app.model import AiVote


class AiVoteService:
    @staticmethod
    def create(image_id: int) -> AiVote:
        vote = AiVote(image_id=image_id)
        AiVote.save(vote)
        return vote

    @staticmethod
    def get_all() -> list[AiVote]:
        return AiVote.find_all()

    @staticmethod
    def get_first() -> AiVote | None:
        return AiVote.find_first()
