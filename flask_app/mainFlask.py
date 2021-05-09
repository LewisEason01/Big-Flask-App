from flask import Flask, render_template, flash, redirect, url_for
from apps.form import LoginForm 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apps.models import User, Post
from apps import app


POSTGRES = {
    'user': 'root',
    'pw': 'superroot',
    'db': 'user_review',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hello'
# db.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
]

    return render_template('index.html', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Creating an object of the class LoginForm
    form = LoginForm()
    # Action once submit button pressed
    if form.validate_on_submit():
        # Flash used for displaying messages on a webpage
        flash('Login requested for user {}, remember me={}'.format(
            form.username.data, form.remember_me.data))
            # directs user to 'index' page
        return redirect(url_for(('index')))

    return render_template('login.html', title='Sign In', form=form)

# @app.route('/homepage', methods=['GET', 'POST'])
# def homepage():
#     homepage = LoginForm()
#     user = homepage.username.data
#     return render_template('homepage.html', user=user)

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(host='127.0.0.1', port=8001)