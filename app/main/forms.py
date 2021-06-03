from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class ReviewForm(FlaskForm):
    """Class to contain forms instances and methods"""
    title = StringField('Review title', validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')