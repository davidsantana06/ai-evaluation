from google.genai import Client
from google.genai.types import GenerateContentConfig, GenerateContentResponse
from io import BytesIO

from app.config import Parameter

from .base import ExternalAiService


class GeminiAiService(ExternalAiService):
    __client = Client(api_key=Parameter.GEMINI_AI_KEY)
    __config = GenerateContentConfig(response_modalities=["TEXT", "IMAGE"])

    @classmethod
    def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        def submit_prompt():
            return cls.__client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=f"{prompt} with {width}x{height} pixels resolution",
                config=cls.__config,
            )

        def extract(generation: GenerateContentResponse):
            parts = generation.candidates[0].content.parts
            image_part = next((p for p in parts if p.inline_data))
            return image_part.inline_data.data

        generation = submit_prompt()
        content = extract(generation)
        return cls._decode(content)
