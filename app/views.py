from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm, EditForm
from models import User, ROLE_USER, ROLE_ADMIN, Event, Market, Selection
from datetime import datetime
from config import POSTS_PER_PAGE, MAX_SEARCH_RESULTS

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

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
@app.route('/index/<int:page>', methods = ['GET', 'POST'])
@login_required
def index(page = 1):
    events = Event.query.all()
    markets = Market.query.all()
    return render_template('index.html',
        title = 'Home',
        events = events,
        markets = markets)

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        nickname = User.make_unique_nickname(nickname)
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    if 'betslip' in session:
    	session.pop('betslip', None)
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/user/<nickname>')
@app.route('/user/<nickname>/<int:page>')
@login_required
def user(nickname, page = 1):
    user = User.query.filter_by(nickname = nickname).first()
    if user == None:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
	return render_template('user.html', user = user)

@app.route('/edit', methods = ['GET', 'POST'])
@login_required
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    elif request.method != "POST":
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
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
    print selection.name
    return redirect(url_for('market', id = selection.market.id))

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
        db.session.commit()
    session.pop('betslip', None)
    return redirect(url_for('index'))