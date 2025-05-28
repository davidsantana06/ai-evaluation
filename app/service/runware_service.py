from io import BytesIO
from runware import Runware, IImageInference
import requests

from app.config import Parameter

from .base import ExternalAiService


class RunwareService(ExternalAiService):
    _client = Runware(api_key=Parameter.RUNWARE_AI_KEY)
    __is_connected = False

    @classmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        if not cls.__is_connected:
            await cls._client.connect()
            cls.__is_connected = True

        request_image = IImageInference(
            positivePrompt=prompt,
            model="civitai:101055@128078",
            numberResults=1,
            width=width,
            height=height,
        )
        answer = await cls._client.imageInference(request_image)
        url = answer[0].imageURL
        response = requests.get(url)
        return BytesIO(response.content)
