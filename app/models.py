from hashlib import md5
from app import db
from app import app

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    bets = db.relationship('Bet', backref = 'punter', lazy = 'dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    
    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname = nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new_nickname).first() == None:
                break
            version += 1
        return new_nickname
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)
                
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
    