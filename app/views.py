from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.security import LoginForm, current_user, login_required, login_user
from app import app, db
from forms import EditForm, RegisterForm
from models import User, Event, Market, Selection, Bet
from datetime import datetime

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@login_required
def index():
    events = Event.query.all()
    markets = Market.query.all()
    return render_template('index.html',
        title = 'Home',
        events = events,
        markets = markets)



@app.route('/user/<email>')
@login_required
def user(email):
    user = User.query.filter_by(email = email).first()
    if user == None:
        flash('User ' + email + ' not found.')
        return redirect(url_for('index'))
    return render_template('user.html', user = user)

@app.route('/edit', methods = ['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.email)
    if form.validate_on_submit():
        g.user.email = form.email.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    elif request.method != "POST":
        form.nickname.data = g.user.email
    return render_template('edit.html',
        form = form)

        
@app.route('/market/<id>')
@login_required
def market(id):
    selections = Selection.query.filter_by(market_id = id).order_by(Selection.selected_count.desc()).all()
    return render_template('market.html', selections = selections)

@app.route('/add/<id>')
@login_required
def add(id):
    selection = Selection.query.filter_by(id = id).first()
    #session['betslip'].append(selection)
    if 'betslip' in session:
    	session['betslip'] += [selection]
    else: 
    	session['betslip'] = []
    	session['betslip'] += [selection]
    print 'here'
    print selection.name
    return redirect(url_for('index'))

@app.route('/clear_bets')
@login_required
def clear_bets():
    if 'betslip' in session:
    	session.pop('betslip', None)
    return redirect(url_for('index'))
    
@app.route('/confirm_bets')
@login_required
def confirm_bets():
    for selection in session['betslip']:
        print selection.name
        m = Market.query.get(selection.market_id)
        m.pool += 1
        s = Selection.query.get(selection.id)
        s.selected_count += 1
        db.session.add(Bet(state='Pending', timestamp=datetime.utcnow(), punter=g.user, selected=s))
        u = User.query.get(g.user.id)
        u.balance -= 1
        db.session.commit()
    session.pop('betslip', None)
    return redirect(url_for('index'))
