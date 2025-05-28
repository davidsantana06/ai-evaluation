from abc import ABC, abstractmethod
from io import BytesIO


class ExternalAiService(ABC):
    _client = None

    @classmethod
    @abstractmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        pass
