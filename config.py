import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-chgchg-guess'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'coreyprj@gmail.com'
MAIL_PASSWORD = 'vckhbwspnobbnvjr'

# administrator list
ADMINS = ['coreyprj@gmail.com']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

# flask-security
SECURITY_REGISTERABLE = True
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'gharthsrthrthddfsrtje475j'