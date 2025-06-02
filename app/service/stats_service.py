from collections import defaultdict

from app.model import Image
from app.service.image_service import ImageService
from app.typing import StatsSummary


class StatsService:
    @staticmethod
    def __add_image_generated(image: Image, generated_images: dict[str, int]) -> None:
        generated_images[image.ai] += 1

    @staticmethod
    def __add_ai_vote(image: Image, ai_votes: dict[str, int]) -> None:
        has_been_voted = image.ai_vote is not None
        if not has_been_voted:
            return

        ai_votes[image.ai] += 1

    @staticmethod
    def __add_human_vote(image: Image, human_votes: dict[str, int]) -> None:
        has_been_voted = image.human_vote is not None
        if not has_been_voted:
            return

        human_votes[image.ai] += 1

    @staticmethod
    def __add_time_taken(image: Image, total_time_taken: dict[str, float]) -> None:
        total_seconds = image.time_taken.total_seconds()
        total_time_taken[image.ai] += total_seconds

    @staticmethod
    def __calculate_average_time_taken(
        total_time_taken: dict[str, float],
        generated_images: dict[str, int],
    ) -> dict[str, float]:
        return {
            ai: total_time_taken[ai] / generated_images[ai] for ai in total_time_taken
        }

    @staticmethod
    def __round_values(data: dict[str, float]) -> dict[str, float]:
        return {key: round(value, 2) for key, value in data.items()}

    @classmethod
    def summarize(cls) -> StatsSummary:
        generated_images = defaultdict(int)
        ai_votes = defaultdict(int)
        human_votes = defaultdict(int)
        total_time_taken = defaultdict(float)

        images = ImageService.get_all()

        for image in images:
            cls.__add_image_generated(image, generated_images)
            cls.__add_ai_vote(image, ai_votes)
            cls.__add_human_vote(image, human_votes)
            cls.__add_time_taken(image, total_time_taken)

        average_time_taken = cls.__calculate_average_time_taken(
            total_time_taken,
            generated_images,
        )

        return {
            "generated_images": {
                "description": "Quantidade de imagens geradas",
                "data": generated_images,
            },
            "ai_votes": {
                "description": (
                    "Quantidade de votos feitos pelo ChatGPT. "
                    + "IA sem voto NÃO é contabilizada"
                ),
                "data": ai_votes,
            },
            "human_votes": {
                "description": (
                    "Quantidade de votos feitos por você. "
                    + "IA sem voto NÃO é contabilizada"
                ),
                "data": human_votes,
            },
            "total_time_taken": {
                "description": "Tempo total para a geração das imagens, em segundos",
                "data": cls.__round_values(total_time_taken),
            },
            "average_time_taken": {
                "description": "Tempo médio para a geração das imagens, em segundos",
                "data": cls.__round_values(average_time_taken),
            },
        }
