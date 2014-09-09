import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask_beaker import BeakerSession
from flask.ext.security import Security, SQLAlchemyUserDatastore, current_user
from flask.ext.admin import Admin
from flask.ext.admin.contrib import sqla
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from momentjs import momentjs

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
mail = Mail(app)
BeakerSession(app)
admin = Admin(app)

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'cjbet failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/cjbet.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('cjbet startup')

app.jinja_env.globals['momentjs'] = momentjs

from app import views, models
from models import User, Role, Selection, Market, Event
# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Setup model admin
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        if current_user.is_authenticated():
            return current_user.has_role('admin') 
        return False
    
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(Event, db.session))
admin.add_view(MyModelView(Market, db.session))
admin.add_view(MyModelView(Selection, db.session))