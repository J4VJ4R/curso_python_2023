from flask import Blueprint, render_template, request
from .models import Post, User
from blog.language import get_language

bp = Blueprint('home', __name__)

#obtener usuario
def get_user(id):
  user = User.query.get_or_404(id)
  return user
#configuración del buscador
def search_data(query):
  posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()
  return posts
#index without lang
@bp.route('/', methods = ['GET', 'POST'])
def index():
  posts = Post.query.all()
  if request.method == 'POST':
    query = request.form.get('search')
    posts = search_data(query)
    value = 'hidden'
    return indexlang('es', posts, value)
  return indexlang('es', posts)
#index with lang
# @bp.route('/', methods = ['GET', 'POST'])
# def index():
#   posts = Post.query.all()
#   if request.method == 'POST':
#     query = request.form.get('search')
#     posts = search_data(query)
#     value = 'hidden'
#     return render_template('index.html', posts = posts, get_user = get_user, value = value)
#   return render_template('index.html', posts = posts, get_user = get_user)
#index with language
@bp.route('/<lang>', methods = ['GET', 'POST'])
def indexlang(lang, posts=None, value=None):
  messages = get_language(lang)
  posts = Post.query.all()
  if request.method == 'POST':
    query = request.form.get('search')
    posts = search_data(query)
    value = 'hidden'
    return render_template('index.html', messages = messages, lang = lang,
                            posts = posts, get_user = get_user, value = value)
  return render_template('index.html', posts = posts, get_user = get_user,
                          messages = messages, lang = lang)
#mostrar el blog
@bp.route('/blog/<url>')
def blog(url):
  post = Post.query.filter_by(url = url).first()
  return render_template('blog.html', post = post, get_user = get_user)