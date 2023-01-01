from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, URL, Regexp
from wtforms.widgets import TextArea

class MatrixForm(FlaskForm):
    matrix = TextAreaField('Matrix', widget=TextArea())
    submit = SubmitField('Compute')

