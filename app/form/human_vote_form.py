from flask_wtf import FlaskForm
from wtforms import RadioField


class HumanVoteForm(FlaskForm):
    image_id = RadioField()
