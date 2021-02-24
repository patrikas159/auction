from wtforms import Form, StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class registration_form(Form):
    email = StringField("Please input your email", validators=[DataRequired(), Email()])
    username = StringField("Please input your username", validators=[DataRequired()])
    password = PasswordField("input password", validators=[DataRequired()])
    submit = SubmitField("Submit")