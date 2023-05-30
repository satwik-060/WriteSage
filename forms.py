'''Forms'''
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):  
    """Registration Form"""
    username = StringField('Username' ,validators=[DataRequired(),
                                       Length(min = 2 , max = 20)])
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = StringField('Password' , validators = [DataRequired()])
    confirm_password = StringField('Confirm Password',validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    """Login Form"""
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = StringField('Password' , validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
