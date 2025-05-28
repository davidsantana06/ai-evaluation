from google.genai import Client
from google.genai.types import GenerateContentConfig
from io import BytesIO

from app.config import Parameter

from .base import ExternalAiService


class GeminiAiService(ExternalAiService):
    _client = Client(api_key=Parameter.GEMINI_AI_KEY)

    @classmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        answer = cls._client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=f"{prompt} with {width}x{height} resolution",
            config=GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
        )
        parts = answer.candidates[0].content.parts
        image_part = next(
            (part for part in parts if part.inline_data),
            None,
        )
        return BytesIO(image_part.inline_data.data)
