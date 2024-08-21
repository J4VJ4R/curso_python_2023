from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from blog.auth import login_required
from .models import Post
from blog import db
from datetime import datetime

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/posts')
@login_required
def posts():
  return render_template('admin/posts.html')

@bp.route('/create', methods = ('GET', 'POST'))
@login_required
def create():
  if request.method == 'POST':
    #obtenemos datos
    url = request.form.get('url')
    title = request.form.get('title')
    desc = request.form.get('desc')
    content = request.form.get('content')
    datetimenow = datetime.utcnow
    #construimos un objeto post
    post = Post(g.user.id, url, title, desc, content, datetimenow)
    #validación de datos
    error = None
    #comparamos url con las existentes en la base de datos
    url = Post.query.filter_by(url = url).first()
    if url == None:
      #se guarda el post
      db.session.add(post)
      db.session.commit()
      #redirige a posts
      return redirect(url_for('post.posts'))
    else:
      error = f'La url {url} ya está registrada, prueba otra'
    flash(error)
  return render_template('admin/create.html')

@bp.route('/update')
@login_required
def update():
  return render_template('admin/update.html')