from hashlib import md5
from app import db
from app import app
from flask.ext.security import UserMixin, RoleMixin

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(20), unique = True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    bets = db.relationship('Bet', backref = 'punter', lazy = 'dynamic')
    balance = db.Column(db.Float(), default = 0)
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(20))
    current_login_ip = db.Column(db.String(20))
    login_count = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    
    def get_id(self):
        return unicode(self.id)

    def __str__(self):
        return '<User id=%s email=%s>' % (self.id, self.email)
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)    
        
class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    start = db.Column(db.DateTime)
    is_locked = db.Column(db.Boolean, default = False)
    markets = db.relationship('Market', backref = 'event', lazy = 'dynamic')
    # has many markets

class Market(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    pool = db.Column(db.Float, default = 0)
    is_locked = db.Column(db.Boolean, default = False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    selections = db.relationship('Selection', backref = 'market', lazy = 'dynamic')
    
    def selections_by_divd(self):
        return Selection.query.filter_by(market_id = self.id).order_by(Selection.selected_count.desc()).all()
	
class Selection(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    selected_count = db.Column(db.Integer, default = 0)
    is_winner = db.Column(db.Boolean, default = False)
    market_id = db.Column(db.Integer, db.ForeignKey('market.id'))
    bets = db.relationship('Bet', backref = 'selected', lazy = 'dynamic')
    
    def dividend(self):
    	if self.selected_count > 0:
    		return float(self.market.pool / self.selected_count)
    	else:
    		return self.market.pool
        
    def market_name(self):
        return Market.query.get(self.market_id).name
    
class Bet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    state = db.Column(db.String(64)) # pending, win, loss
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    selection_id = db.Column(db.Integer, db.ForeignKey('selection.id'))
    