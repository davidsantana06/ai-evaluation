from io import BytesIO
from openai import OpenAI
from openai.types.images_response import ImagesResponse
from openai.types.chat.chat_completion import ChatCompletion

from app.config import Parameter
from app.model import Image

from .base import ExternalAiService


class OpenAiService(ExternalAiService):
    __client = OpenAI(api_key=Parameter.OPEN_AI_KEY)

    @classmethod
    async def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        def submit_prompt():
            return cls.__client.images.generate(
                model="dall-e-2",
                prompt=prompt,
                size=f"{width}x{height}",
                n=1,
            )

        def extract(generation: ImagesResponse):
            return generation.data[0].url

        generation = submit_prompt()
        url = extract(generation)
        return cls._download(url)

    @classmethod
    def evaluate_images(cls, images: list[Image]) -> int:
        def _embed(image: Image):
            return [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{image.base64}"},
                },
                {
                    "type": "text",
                    "text": str(image.id),
                },
            ]

        def _compose_prompt():
            return [
                {
                    "type": "text",
                    "text": (
                        "Analyze the images and respond with the "
                        "number of the best one, only the number."
                    ),
                }
            ] + [_embed(image) for image in images]

        def submit_prompt():
            prompt = _compose_prompt()
            return cls.__client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages={"role": "user", "content": prompt},
                max_tokens=1,
            )

        def extract(completion: ChatCompletion):
            content = completion.choices[0].message.content.strip()
            return int(content)

        completion = submit_prompt()
        return extract(completion)
