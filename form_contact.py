from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()


class ContactForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Поле Имя не может быть пустым')])
    email = StringField('E-mail', validators=[DataRequired('Поле E-mail не может быть пустым'), Email()])
    subject = StringField('Тема', validators=[DataRequired('Поле Тема не может быть пустым')])
    message = TextAreaField('Сообщение', validators=[DataRequired('Поле Сообщение не может быть пустым')])
    submit = SubmitField("Отправить")