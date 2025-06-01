from datetime import timedelta
from os.path import join
from uuid import uuid4

from app.config import Path
from app.model import Image


class ImageService:
    DEFAULT_WIDTH = 1024
    DEFAULT_HEIGHT = 1024

    @staticmethod
    def create(
        group: int,
        theme: str,
        ai: str,
        prompt: str,
        base64: str,
        filename: str,
        time_taken: timedelta,
    ) -> Image:
        image = Image(
            group=group,
            theme=theme,
            ai=ai,
            prompt=prompt,
            base64=base64,
            filename=filename,
            time_taken=time_taken,
        )
        Image.save(image)
        return image

    @staticmethod
    def get_all() -> list[Image]:
        return Image.find_all()

    @staticmethod
    def get_all_by_group(group: int) -> list[Image]:
        return Image.find_all_by_group(group)

    @staticmethod
    def get_one_by_group(group: int) -> Image | None:
        return Image.find_first_by_group(group)

    @staticmethod
    def get_one_by_id(id: int) -> Image | None:
        return Image.find_first_by_id(id)

    @staticmethod
    def __generate_filename() -> str:
        return f"{uuid4()}.png"

    @classmethod
    def save_as_png(cls, binary: bytes) -> str:
        filename = cls.__generate_filename()
        filepath = join(Path.IMAGE_FOLDER, filename)
        with open(filepath, "wb") as file:
            file.write(binary)
        return filename
