from flask import (
  Blueprint, render_template, request, url_for, redirect, flash, session, g
  )
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from todor import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods = ('GET', 'POST'))
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    user = User(username, generate_password_hash(password))
    #manejo de errores
    error = None
    user_name = User.query.filter_by(username = username).first()
    if user_name == None:
      db.session.add(user)
      db.session.commit()
      return redirect(url_for('auth.login'))
    else:
      error = f'El usuario {username} ya está registrado'
    flash(error)
  return render_template('auth/register.html')

@bp.route('/login', methods = ('GET', 'POST'))
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']

    #manejo de errores
    error = None
    #validar datos
    user = User.query.filter_by(username = username).first()
    if user == None:
      error = "El nombre de usuario es incorrecto"
    elif not check_password_hash(user.password, password):
      error = "Contraseña incorrecta"
    #iniciar sesión
    if error == None:
      session.clear()
      session['user_id'] = user.id
      return redirect(url_for('todo.index'))
    
    flash(error)
  return render_template('auth/login.html')

#mantener sesión iniciada
@bp.before_app_request #Se verifica sesión antes de abrir cada modulo
def load_logged_in_user():
  user_id = session.get('user_id')
  if user_id is None:
    g.user = None
  else:
    g.user = User.query.get_or_404(user_id)