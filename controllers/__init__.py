from controllers.blog_api import blog_api
from controllers.test_api import test_api
from controllers.auth_api import auth_api
from flask import Flask


def setup_controllers(app: Flask):
    app.register_blueprint(blog_api, url_prefix="/blog")
    app.register_blueprint(auth_api, url_prefix="/auth")
    app.register_blueprint(test_api, url_prefix="/test")

