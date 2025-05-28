from io import BytesIO
import requests
from openai import OpenAI

from app.config import Parameter
from app.model import Image

from .base import ExternalAiService


class OpenAiService(ExternalAiService):
    _client = OpenAI(api_key=Parameter.OPEN_AI_KEY)

    @classmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        answer = cls._client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size=f"{width}x{height}",
            n=1,
            output_format="png",
            moderation="auto",
        )
        url = answer.data[0].url
        response = requests.get(url)
        return BytesIO(response.content)

    @classmethod
    def evaluate_images(cls, images: list[Image]) -> int:
        question_content = [
            {
                "type": "text",
                "text": "Analyze the images and respond with the number of the best one, only the number.",
            }
        ]

        for image in images:
            image_url = {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{image.base64}"},
            }
            text = {"type": "text", "text": str(image.id)}
            question_content.extend([image_url, text])

        answer = cls._client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages={"role": "user", "content": question_content},
            max_tokens=1,
        )
        answer_content = answer.choices[0].message.content.strip()
        return int(answer_content)
