from app.model import Image


class ImageService:
    DEFAULT_WIDTH = 512
    DEFAULT_HEIGHT = 512

    @staticmethod
    def create(
        group: int,
        theme: str,
        ai: str,
        prompt: str,
        base64: str,
        filename: str,
    ) -> Image:
        image = Image(
            group=group,
            theme=theme,
            ai=ai,
            prompt=prompt,
            base64=base64,
            filename=filename,
        )
        Image.save(image)
        return image

    @staticmethod
    def get_all() -> list[Image]:
        return Image.find_all()

    @staticmethod
    def get_one_by_group(group: int) -> Image | None:
        return Image.find_first_by_group(group)
