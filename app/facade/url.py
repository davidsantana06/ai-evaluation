from caseconverter import pascalcase
from flask import url_for


class Url:
    @staticmethod
    def for_static(filename: str) -> str:
        return url_for("static", filename=filename)

    @staticmethod
    def for_view(endpoint: str, **values: object) -> str:
        module, method = endpoint.split(":")
        class_ = pascalcase(module) + "View"
        return url_for(f"{class_}:{method}", **values)
