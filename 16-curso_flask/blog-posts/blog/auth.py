from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from blog import db
import functools
from werkzeug.utils import secure_filename
from blog.language import get_language

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register/<lang>', methods = ('GET', 'POST'))
def register(lang):
  messages = get_language(lang)
  if request.method == 'POST':
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    #construimos un objeto user
    user = User(username, email, generate_password_hash(password))
    #validación de datos
    error = None
    #comparando nombre de usuario con los existentes en la base de datos
    user_email = User.query.filter_by(email = email).first()
    if user_email == None:
      db.session.add(user)
      #guardar datos
      db.session.commit()
      #redirige a login
      return redirect(url_for('auth.login', lang=lang))
    else:
      if lang == 'es':
        error = f'El correo {email} ya está registrado'
      elif lang == 'en':
        error = f'The email {email} is already registered'

    flash(error)
  return render_template('auth/register.html', messages = messages, lang = lang)

@bp.route('/login/<lang>', methods = ('GET', 'POST'))
def login(lang):
  messages = get_language(lang)
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    #validación de los datos con base de datos
    error = None
    user = User.query.filter_by(email = email).first()
    #comparamos los datos
    if user == None or not check_password_hash(user.password, password):
      if lang == 'es':
        error = 'Correo or contraseña incorrecta'
      elif lang == 'en':
        error = 'Wrong password o email'        
    #iniciando sesión
    if error is None:
      session.clear()
      session['user_id'] = user.id
      return redirect(url_for('post.posts', lang=lang))
    flash(error)
  return render_template('auth/login.html', messages = messages, lang = lang)
#cargar el inicio de sesión
@bp.before_app_request
def load_logged_in_user():
  user_id = session.get('user_id')
  #commprobación
  if user_id is None:
    g.user = None
  else:
    g.user = User.query.get_or_404(user_id)
#para salir del aplicativo
@bp.route('/logout/<lang>')
def logout(lang):
  messages = get_language(lang)
  session.clear()
  return redirect(url_for('home.index', lang = lang))
#para requerir iniciar sesión
def login_required(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
    if g.user is None:
      return redirect(url_for('auth.login'))
    return view(**kwargs)
  return wrapped_view
@bp.route('/profile/<int:id>/<lang>', methods = ('GET', 'POST'))
#autenticación requerida
@login_required
def profile(id, lang):
  messages = get_language(lang)
  #se obtiene el usuario
  user = User.query.get_or_404(id)
  if request.method == 'POST':
    user.username = request.form.get('username')
    password = request.form.get('password')
    #validamos los datos
    error = None
    if len(password) != 0:
      user.password = generate_password_hash(password)
    elif len(password) > 0 and len(password) < 6:
      error = 'La contraseña debe tener más de 6 caracteres'
    #Para las imágenes
    if request.files['photo']:
      img = request.files['photo']
      img.save(f'blog/static/media/{secure_filename(img.filename)}')
      user.img = f'media/{secure_filename(img.filename)}'
    if error is not None:
      flash(error)
    else:
      db.session.commit()
      return redirect(url_for('auth.profile', id = user.id, messages = messages, lang = lang))
    flash(error)  
  return render_template('auth/profile.html', user = user, messages = messages, lang = lang)