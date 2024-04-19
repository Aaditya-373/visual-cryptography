from flask_wtf import FlaskForm
from wtforms import StringField,HiddenField,PasswordField
from wtforms.validators import DataRequired


class UserQrScan(FlaskForm):
    qr = HiddenField('qr', validators=[DataRequired()])

class BookQrScan(FlaskForm):
    qr = HiddenField('qr', validators=[DataRequired()])

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

