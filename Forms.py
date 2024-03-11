from flask_wtf import FlaskForm
from wtforms import StringField, PassField, SubbmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username=StringField('Username',
                         validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Email',
                      validators=[DataRequired(), Email()])
    password=PassField('Password',
                       validators=[DataRequired()])
    confirm_password=PassField('Password', 
                       validators= [DataRequired(),EqualTo('password')])
    submit= SubbmitField('Sign-Up')


    class LoginForm(FlaskForm):
    
    email=StringField('Email',
                      validators=[DataRequired(), Email()])
    password=PassField('Password',
                       validators=[DataRequired()])
   
    submit= SubbmitField('Login')