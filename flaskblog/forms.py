'''Forms'''
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):  
    """Registration Form"""
    username = StringField('Username' ,validators=[DataRequired(),
                                       Length(min = 2 , max = 20)])
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = StringField('Password' , validators = [DataRequired()])
    confirm_password = StringField('Confirm Password',validators = [DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already in use.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("An account is already created with this Email. Please create another email account to create an account here.")
        
class LoginForm(FlaskForm):
    """Login Form"""
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = StringField('Password' , validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):  
    """Registration Form"""
    username = StringField('Username' ,validators=[DataRequired(),
                                       Length(min = 2 , max = 20)])
    email = StringField('Email', validators = [DataRequired(),Email()])

    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already in use.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("An account is already created with this Email. Please create another email account to create an account here.")