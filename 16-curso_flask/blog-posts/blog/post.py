from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from blog.auth import login_required
from .models import Post
from blog import db
from datetime import datetime
from blog.language import get_language

bp = Blueprint('post', __name__, url_prefix='/post')

@bp.route('/posts/<lang>')
@login_required
def posts(lang):
  messages = get_language(lang)
  allposts = Post.query.all()
  return render_template('admin/posts.html', allposts = allposts, messages = messages, lang = lang)

@bp.route('/create/<lang>', methods = ('GET', 'POST'))
@login_required
def create(lang):
  messages = get_language(lang)
  if request.method == 'POST':
    #obtenemos datos
    url = request.form.get('url')
    url = url.replace(' ', '-')
    title = request.form.get('title')
    info = request.form.get('info')
    content = request.form.get('content')
    datetimenow = datetime.utcnow
    #construimos un objeto post
    post = Post(g.user.id, url, title, info, content, datetimenow)
    #validación de datos
    error = None
    #comparamos url con las existentes en la base de datos
    post_url = Post.query.filter_by(url = url).first()
    if post_url == None:
      #se guarda el post
      db.session.add(post)
      db.session.commit()
      flash(f'El blog {post.title} se creó correctamente')
      #redirige a posts
      return redirect(url_for('post.posts', lang = lang))
    else:
      error = f'La url {post_url} ya está registrada, prueba otra'
    flash(error)
  return render_template('admin/create.html', messages = messages, lang = lang)
#obtener post
def get_post(id):
  post = Post.query.get_or_404(id)
  return post
@bp.route('/update/<int:id>/<lang>', methods = ('GET', 'POST'))
@login_required
def update(id, lang):
  messages = get_language(lang)
  post = get_post(id)
  if request.method == 'POST':
    post.title = request.form.get('title')
    post.info = request.form.get('info')
    post.content = request.form.get('content')
    #efectuamos cambios
    db.session.commit()
    error = None
    error = f'El blog {post.title} se actualizó correctamente'
    flash(error)
    return redirect(url_for('post.posts', lang = lang))
  return render_template('admin/update.html', post = post, messages = messages, lang = lang)
#eliminar post
@bp.route('/delete/<int:id>/<lang>')
@login_required
def delete(id, lang):
  messages = get_language(lang)
  #obtenemos el post
  post = get_post(id)
  if post:
    #se elimina el post
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('post.posts', lang = lang))
  else:
    return redirect(url_for('post.posts', lang = lang))