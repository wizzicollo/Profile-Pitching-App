from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, SelectField,TextAreaField
from wtforms.validators import Required

class InForm(FlaskForm):
    pitch = TextAreaField('Tell it')
    title = StringField('Title')
    category = SelectField(u'info category', choices=[('life', 'life'), ('coding', 'coding'), ('funny', 'funny'), ('love', 'love'), ('philosophy', 'philosophy'), ('wisdom', 'wisdom')])
    submit = SubmitField('Submit')

 
class lamentform(FlaskForm):
    comment = TextAreaField('lament')
    submit = SubmitField('Post lamentations')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('What is interesting about you', validators=[Required()])
    submit = SubmitField('submit')
    