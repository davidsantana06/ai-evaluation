from app.model import Image


class ImageService:
    @staticmethod
    def create(group: int, theme: str, ai: str, prompt: str, filename: str) -> Image:
        image = Image(group, theme, ai, prompt, filename)
        Image.save(image)
        return image

    @staticmethod
    def get_all() -> list[Image]:
        return Image.find_all()

    @staticmethod
    def get_one_by_group(group: int) -> Image | None:
        return Image.find_first_by_group(group)
