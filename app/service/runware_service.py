from io import BytesIO
from runware import Runware, IImageInference
from runware.types import IImage

from app.config import Parameter

from .base import ExternalAiService


class RunwareService(ExternalAiService):
    __client = Runware(api_key=Parameter.RUNWARE_KEY)

    @classmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        async def connect_once():
            is_connected = cls.__client.connected()
            if is_connected:
                return

            await cls.__client.connect()
            cls.__is_connected = True

        async def submit_prompt():
            request = IImageInference(
                positivePrompt=prompt,
                model="civitai:101055@128078",
                numberResults=1,
                width=width,
                height=height,
            )
            return await cls.__client.imageInference(request)

        def extract(generation: list[IImage]):
            return generation[0].imageURL

        await connect_once()
        generation = await submit_prompt()
        url = extract(generation)
        return cls._download(url)
