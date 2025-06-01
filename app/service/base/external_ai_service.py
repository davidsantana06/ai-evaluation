from abc import ABC, abstractmethod
from io import BytesIO
from requests import Response, get, post


class ExternalAiService(ABC):
    @staticmethod
    def _get(url: str) -> Response:
        return get(url)

    @staticmethod
    def _post(url: str, headers: dict, body: dict) -> Response:
        return post(url, headers=headers, data=body, files={"none": ""})

    @staticmethod
    def _decode(data: bytes) -> BytesIO:
        return BytesIO(data)

    @classmethod
    def _download(cls, url: str) -> BytesIO:
        response = cls._get(url)
        data = response.content
        return cls._decode(data)

    @classmethod
    @abstractmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        pass
