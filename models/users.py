from flask import request
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    number = db.Column(db.Integer(), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, email, password, name, number, admin):
        self.email = email
        self.name = name
        self.number = number
        self.admin = admin
        self.password = generate_password_hash(password)

    def check_pass(self, password):
        return check_password_hash(self.password, password)
