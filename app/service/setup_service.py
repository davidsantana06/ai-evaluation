from base64 import b64encode
from datetime import datetime
from io import BytesIO
from random import sample
import json

from app.config import Path
from app.model import Image
from app.typing import Ai, GenerationEntry

from .gemini_ai_service import GeminiAiService
from .image_service import ImageService
from .open_ai_service import OpenAiService
from .runware_service import RunwareService
from .stability_ai_service import StabilityAiService


class SetupService:
    @staticmethod
    def get_generation_entries() -> list[GenerationEntry]:
        with open(Path.GENERATION_ENTRIES_FILE, "r") as file:
            return json.load(file)

    @staticmethod
    def randomize_ais() -> list[Ai]:
        return sample(
            [Ai.GEMINI, Ai.OPENAI, Ai.RUNWARE, Ai.STABILITY_AI],
            k=4,
        )

    @classmethod
    def __generate_image(cls, ai: Ai, prompt: str) -> BytesIO:
        service = {
            Ai.GEMINI: GeminiAiService,
            Ai.OPENAI: OpenAiService,
            Ai.RUNWARE: RunwareService,
            Ai.STABILITY_AI: StabilityAiService,
        }
        buffer = service[ai].generate_image(
            prompt,
            ImageService.DEFAULT_WIDTH,
            ImageService.DEFAULT_HEIGHT,
        )
        return buffer.getvalue()

    @classmethod
    def create_image(
        cls,
        ai: str,
        group: int,
        theme: str,
        prompt: str,
    ) -> Image:
        start_time = datetime.now()
        binary = cls.__generate_image(ai, prompt)
        base64 = b64encode(binary).decode("utf-8")
        filename = ImageService.save_as_png(binary)
        end_time = datetime.now()
        time_taken = end_time - start_time
        return ImageService.create(
            group,
            theme,
            ai,
            prompt,
            base64,
            filename,
            time_taken,
        )
