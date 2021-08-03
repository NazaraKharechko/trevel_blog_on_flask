from flask_login import UserMixin
from app import db


class Blog(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), unique=True)
    text = db.Column(db.String(1000))
    img_src = db.Column(db.String(1000))
    teg = db.Column(db.String(1000))

    def __init__(self, city, text, img_src, teg):
        self.city = city
        self.text = text
        self.img_src = img_src
        self.teg = teg
