from io import BytesIO
from requests import Response, post

from app.config import Parameter
from .base import ExternalAiService


class StabilityAiService(ExternalAiService):
    __API_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"
    __HEADERS = {
        "authorization": f"Bearer {Parameter.STABILITY_AI_KEY}",
        "accept": "image/*",
    }

    @classmethod
    def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        def submit_prompt():
            return post(
                cls.__API_URL,
                headers=cls.__HEADERS,
                data={"prompt": f"{prompt} with {width}x{height} pixels resolution"},
                files={"none": ""},
            )

        def extract(generation: Response):
            return generation.content

        generation = submit_prompt()
        content = extract(generation)
        return cls._decode(content)
