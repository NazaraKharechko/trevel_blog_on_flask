from models import User


def find_user_by_email(user_email: str) -> User:
    return User.query.filter(User.email == user_email).first()
