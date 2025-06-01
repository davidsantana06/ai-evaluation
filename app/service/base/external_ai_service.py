from abc import ABC, abstractmethod
from io import BytesIO
from requests import get


class ExternalAiService(ABC):
    @staticmethod
    def _decode(data: bytes) -> BytesIO:
        return BytesIO(data)

    @classmethod
    def _download(cls, url: str) -> BytesIO:
        response = get(url)
        content = response.content
        return cls._decode(content)

    @classmethod
    @abstractmethod
    def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        pass
