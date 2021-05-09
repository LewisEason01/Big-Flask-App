import os

basedir = os.path.abspath(os.path.dirname(__file__))
# Class where the config items are stored
# Secret key protects the form from CSRF attacks
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hello'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Removes constant notifications of updating database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

