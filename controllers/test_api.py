import logging
from http import HTTPStatus
from flask import Blueprint, request, Flask, templating
from werkzeug.exceptions import abort
import requests as req


test_api = Blueprint("test_api", __name__)


@test_api.route("/", methods=["GET", "POST"])
def index():
    try:
        resp = req.get('http://localhost:11111/blog/pages')
        print(resp.text)
        if '&lt;script&gt;console.log(1)&lt;/script&gt;' in resp.text:
            return "BAD", HTTPStatus.BAD_REQUEST
        else:
            return "OK", HTTPStatus.OK
    except Exception as e:
        logging.exception(e)
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
