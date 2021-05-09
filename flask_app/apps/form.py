from flask_wtf import FlaskForm

# wtforms - Form validation and rendering library for python web development
# These are four classes from wtforms for each field
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# Must enter info in text boxes using 'DataRequired validator'
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

