from io import BytesIO
from requests import Response, post
from uuid import uuid4

from app.config import Parameter

from .base import ExternalAiService


class RunwareService(ExternalAiService):
    __API_URL = "https://api.runware.ai/v1"
    __HEADERS = {
        "Authorization": f"Bearer {Parameter.RUNWARE_KEY}",
        "Content-Type": "application/json",
    }

    @classmethod
    def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        def submit_prompt():
            return post(
                cls.__API_URL,
                headers=cls.__HEADERS,
                json=[
                    {
                        "taskType": "imageInference",
                        "taskUUID": str(uuid4()),
                        "positivePrompt": prompt,
                        "width": width,
                        "height": height,
                        "model": "civitai:102438@133677",
                        "numberResults": 1,
                    }
                ],
            )

        def extract(generation: Response):
            data = generation.json()
            return data["data"][0]["imageURL"]

        generation = submit_prompt()
        url = extract(generation)
        return cls._download(url)
