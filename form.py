from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import FileField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class File(FlaskForm):
    file = FileField('图片', validators=[DataRequired()])
    submit = SubmitField('上传')

class DataForm(FlaskForm):
    data = IntegerField('循环次数', validators=[DataRequired()])
    submit = SubmitField('下载结果')