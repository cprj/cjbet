from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo

class UniqueUser(object):
    def __init__(self, message="User exists"):
        self.message = message

    def __call__(self, form, field):
        if current_app.security.datastore.find_user(email=field.data):
            raise ValidationError(self.message)


validators = {
    'email': [
        Required(),
        Email(),
        UniqueUser(message='Email address is associated with '
                           'an existing account')
    ],
    'password': [
        Required(),
        Length(min=6, max=50),
        EqualTo('confirm', message='Passwords must match'),
        Regexp(r'[A-Za-z0-9@#$%^&+=]',
               message='Password contains invalid characters')
    ]
}


class RegisterForm(Form):
    email = TextField('Email', validators['email'])
    password = PasswordField('Password', validators['password'], )
    confirm = PasswordField('Confirm Password')
    
class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
    
    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname
        
    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True
        
class SearchForm(Form):
    search = TextField('search', validators = [Required()])

