from io import BytesIO
from openai import OpenAI
from openai.types.images_response import ImagesResponse
from openai.types.responses import Response


from app.config import Parameter
from app.model import Image

from .base import ExternalAiService


class OpenAiService(ExternalAiService):
    __client = OpenAI(api_key=Parameter.OPENAI_KEY)

    @classmethod
    def generate_image(cls, prompt: str, width: int, height: int) -> BytesIO:
        def submit_prompt():
            return cls.__client.images.generate(
                model="dall-e-3",
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
            return (
                {
                    "image_url": f"data:image/png;base64,{image.base64}",
                    "type": "input_image",
                },
                {
                    "text": str(image.id),
                    "type": "input_text",
                },
            )

        def _compose_prompt():
            return [
                {
                    "text": (
                        "Analyze the images and respond with the "
                        "number of the best one, only the number."
                    ),
                    "type": "input_text",
                },
                *[input_item for image in images for input_item in _embed(image)],
            ]

        def submit_prompt():
            prompt = _compose_prompt()
            return cls.__client.responses.create(
                model="gpt-4.1",
                input=[{"role": "user", "content": prompt}],
            )

        def extract(completion: Response):
            content = completion.output_text
            return int(content)

        completion = submit_prompt()
        return extract(completion)
