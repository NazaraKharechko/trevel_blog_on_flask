from flask import Flask, redirect, url_for
from flask_login import LoginManager
from db import seed_db, db
import os


app = Flask(__name__)
login_manager = LoginManager()


def create_app():
    import logging
    logging.basicConfig(filename='server.log', level=logging.DEBUG)
    app.config["DEBUG"] = os.environ.get("DEBUG", "False").lower() in ["true", "1", "t"]
    app.config["URL_PREFIX"] = ("/" + os.environ.get("URL_PREFIX", "")) if not app.config["DEBUG"] else ""
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret_key")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI", 'sqlite:///db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    db.init_app(app)

    from controllers import setup_controllers
    setup_controllers(app)

    login_manager.login_view = 'auth_api.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def hello_world():
        return redirect(url_for("blog_api.blog"))

    @app.context_processor
    def override_url_for():
        return dict(url_for=prefixed_url_for)

    def prefixed_url_for(endpoint, **values):
        url = url_for(endpoint, **values)
        return f"{app.config['URL_PREFIX']}{url}"

    app.app_context().push()
    seed_db()
    return app
