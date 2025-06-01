from io import BytesIO
from requests import Response

from app.config import Parameter
from .base import ExternalAiService


class StabilityAiService(ExternalAiService):
    __API_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"
    __HEADERS = {
        "authorization": f"Bearer {Parameter.STABILITY_AI_KEY}",
        "accept": "image/*",
    }

    @classmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        def submit_prompt():
            return cls._post(
                cls.__API_URL,
                cls.__HEADERS,
                {"prompt": f"{prompt} with {width}x{height} pixels resolution"},
            )

        def extract(generation: Response):
            return generation.content

        generation = submit_prompt()
        data = extract(generation)
        return cls._decode(data)
