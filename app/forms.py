from flask_uploads import UploadSet #puede ser este el error
from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Incorrect email')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    adress = StringField('Adress', validators=[DataRequired()])
    institution = StringField('Institution', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already in use, please use a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already in use, please use a different one.')

#EVA'S CHANGES, NOT COMPLETELY WORKING BUT NOT COMPLAINING MUCH
class ProteinSeq (FlaskForm):
    """Define the input elements from the query form"""

    def validate_protein (query):
        #function to validate that query sequence has protein format
        aminoacids = "ACDEFGHIKLNMPQRSTVWY"
        validate = True
        str(query)
        for element in query:
            if element not in aminoacids:
                raise ValidationError('Format error, query should be a protein sequence')
                validate = False
                break
        if validate:
            flash('Your query is being processed')

    query = StringField ('Query', validators=[validate_protein("query")])
    file = FileField('File', validators=[validate_protein("query"), FileAllowed(['txt'], '.txt files only!')])
    submit = SubmitField ('Submit')
