from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required

from db import db
from forms.change import BlogForm
from models import Blog

blog_api = Blueprint("blog_api", __name__)


@blog_api.route('/', methods=['GET', 'POST'])
@login_required
def blog():
    blogs = Blog.query.all()
    if request.method == 'POST':
        data = request.form.to_dict()
        city = Blog.query.get(data['id'])
        city.img_src = data.get('img_src', city.img_src)
        city.city = data.get('city', city.city)
        city.text = data.get('text', city.text)
        db.session.commit()
        return redirect(url_for('blog_api.blog'))

    return render_template('blog.html', blogs=blogs, current_user=current_user)


@blog_api.route('/delete/<int:blog_id>', methods=['GET'])
@login_required
def delete_blog(blog_id: int):
    db.session.delete(Blog.query.get(blog_id))
    db.session.commit()
    return redirect(url_for('blog_api.blog'))


@blog_api.route('/add', methods=['GET', 'POST'])
def add():
    form = BlogForm(city='Mexico', img_src='/static/images/img_2.png',
                    text='A Mexican holiday celebrated on May 5th '
                         'is '
                         'Cinco De Mayo, commemorating the victory '
                         'of '
                         'the Battle of Puebla. Dia De Los Reyes, '
                         'which is a Christmastime celebration, '
                         'takes place on January 6th. Semana Santa '
                         'or '
                         '“Holy Week” is when the Latin Catholics '
                         'spend seven days leading up to Easter '
                         'praying.')
    error = None
    data = dict(form.data)
    city = Blog.query.filter_by(city=data['city']).first()

    if request.method == 'POST' and form.validate():
        del data['csrf_token']
        if city:
            error = 'A post with this city name already exists.'
        else:
            blogs = Blog(**data, teg=None)
            db.session.add(blogs)
            db.session.commit()
            return redirect(url_for('blog_api.blog'))
    return render_template('add.html', form=form, error=error)


@blog_api.route('/dad', methods=['GET', 'POST'])
def dad():
    if request.method == 'POST':
        data = request.form.to_dict()
        city = Blog.query.get(data['id'])
        city.teg = data['teg']
        db.session.commit()
        return redirect(url_for('blog_api.blog'))


@blog_api.route('/pages', methods=['GET', 'POST'])
def pages():
    blogs = Blog.query.all()
    return render_template('blog.html', blogs=blogs, current_user=current_user)
