from base64 import b64encode
from io import BytesIO
from typing import Literal, TypedDict
from random import sample
import json

from app.config import Path
from app.model import Image

from .gemini_ai_service import GeminiAiService
from .image_service import ImageService
from .open_ai_service import OpenAiService
from .runware_service import RunwareService
from .stability_ai_service import StabilityAiService


class _GenerationEntry(TypedDict):
    group: int
    theme: str
    prompt: str


class SetupService:
    @staticmethod
    def get_generation_entries() -> list[_GenerationEntry]:
        with open(Path.GENERATION_ENTRIES_FILE, "r") as file:
            return json.load(file)

    @staticmethod
    def randomize_ais() -> list[str]:
        return sample(
            ["Gemini AI", "Open AI", "Runware", "Stability AI"],
            k=4,
        )

    @classmethod
    async def __generate_image(
        cls,
        ai: Literal["Gemini AI", "Open AI", "Runware", "Stability AI"],
        prompt: str,
    ) -> BytesIO:
        service = {
            "Gemini AI": GeminiAiService,
            "Open AI": OpenAiService,
            "Runware": RunwareService,
            "Stability AI": StabilityAiService,
        }
        buffer = await service[ai].generate_image(
            prompt,
            ImageService.DEFAULT_WIDTH,
            ImageService.DEFAULT_HEIGHT,
        )
        return buffer.getvalue()

    @classmethod
    async def create_image(
        cls,
        ai: str,
        group: int,
        theme: str,
        prompt: str,
    ) -> Image:
        binary = await cls.__generate_image(ai, prompt)
        base64 = b64encode(binary).decode("utf-8")
        filename = ImageService.save_as_png(binary)
        image = ImageService.create(group, theme, ai, prompt, base64, filename)
        return image
