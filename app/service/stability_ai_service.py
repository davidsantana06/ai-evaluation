from io import BytesIO
from stability_sdk.client import StabilityInference

from app.config import Parameter

from .base import ExternalAiService


class StabilityAiService(ExternalAiService):
    _client = StabilityInference(key=Parameter.STABILITY_AI_KEY)

    @classmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        answer = next(cls._client.generate(prompt=prompt, width=width, height=height))
        artifact = answer.artifacts[0]
        return BytesIO(artifact.binary)
