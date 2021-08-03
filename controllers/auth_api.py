from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user

from forms.auth import LoginForm
from services.user_service import find_user_by_email

auth_api = Blueprint("auth_api", __name__)


@auth_api.route('/', methods=["GET"])
def index():
    if current_user.is_authenticated == 1:
        return redirect(url_for('blog_api.blog'))
    if current_user.is_authenticated == 0:
        return redirect(url_for('blog_api.login'))
    render_template('base.html', current_user=current_user)


@auth_api.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(email='attacker@gmail.com')
    error = None
    if request.method == 'POST' and login_form.validate():
        data = dict(login_form.data)
        user = find_user_by_email(data['email'])
        if user and user.check_pass(data['password']):
            login_user(user)
            return redirect(url_for('blog_api.blog'))
        if user and user.check_pass(data['password']) == 0:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error, login_form=login_form)


@auth_api.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for("blog_api.blog"))
