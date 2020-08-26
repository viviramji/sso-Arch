import functools

from flask import (
    Blueprint, flash, g, redirect,render_template, request, session, url_for
)
from werkzeug.security import check_password_hash

from app2.db import get_db

db = Blueprint('auth', __name__, url_prefix = '/auth')
@bp.route('/register', methods = ('GET', 'POST'))
def register():
    if request.method == 'POST':
        Username = request.form['Username']
        Password = request.form['Password']
        db = get_db()
        error = None

        if not Username:
            error = 'Username is required'
        elif not Password:
            error = 'Password is required'
        elif db.execute(
            'Select id from user where username = ? ', (Username,)
        ).fetchone() is not None:
             error = 'User {} is already registerd ' .format(Username)

        if error is None:
            db.execute(
                'Insert into user (username, password) values (?, ?)',
                (Username, generate_password_hash(Password))
            )
            db.commit()
            return redirect(url_for('auth.login'))   

        flash(error)
    return render_template('auth/register.html')

@db.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        Username = request.form['Username']  
        Password = request.form['Password']
        db = get_db()
        error = None
        user = db.execute(
            'Select * from user where username = ?', (Username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user['Password'], Password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect (url_for('index'))
        
        flash (error)
    return render_template('auth/login.html')

bp.before_app_request
def load_logged_in_user():
    user_id = session.get ('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'Select * from user where id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view