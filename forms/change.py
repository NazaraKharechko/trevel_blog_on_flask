from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField


class BlogForm(FlaskForm):
    img_src = StringField('Image src')
    city = StringField('City')
    text = TextAreaField('Text')
