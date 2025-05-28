from os.path import abspath, dirname, join


class Path:
    ROOT_FOLDER = abspath(dirname(f"{__file__}/../../../.."))
    """ / """

    ENV_FILE = join(ROOT_FOLDER, ".env")
    """ /.env """

    STATIC_FOLDER = join(ROOT_FOLDER, "static")
    """ /static """

    IMAGE_FOLDER = join(STATIC_FOLDER, "img")
    """ /static/img """

    TEMPLATE_FOLDER = join(ROOT_FOLDER, "template")
    """ /template """

    DATABASE_FILE = join(ROOT_FOLDER, "db.sqlite3")
    """ /db.sqlite3 """
