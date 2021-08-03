from flask_sqlalchemy import SQLAlchemy
from flask import current_app

db = SQLAlchemy()


def seed_db():
    from models import User, Blog
    db.create_all()
    if len(User.query.all()) < 1:
        db.session.add(User(email="attacker@gmail.com",
                            name="Mr Attacker",
                            number="0976707690",
                            admin=False,
                            password="cool_password"))
        db.session.add(User(email="superuser@gmail.com",
                            name="Super User",
                            number="0976707690",
                            admin=True,
                            password="no_one_find_out"))
        db.session.commit()
    if len(Blog.query.all()) < 1:
        db.session.add(Blog(city="London",
                            text="London is the capital and largest city of England and the United Kingdom.",
                            img_src="/static/images/img.png", teg=None))
        db.session.add(Blog(city="Lviv",
                            text="Lviv  is the largest city "
                                 "in western Ukraine and the seventh-largest city in the country overall, "
                                 "with a population of 720,383 Lviv is one of the main cultural "
                                 "centres of Ukraine.",
                            img_src="/static/images/img_1.png", teg=None))
        db.session.commit()
