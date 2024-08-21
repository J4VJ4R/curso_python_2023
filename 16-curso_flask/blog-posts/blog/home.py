from flask import Blueprint, render_template, request
from .models import Post, User

bp = Blueprint('home', __name__)

#obtener usuario
def get_user(id):
  user = User.query.get_or_404(id)
  return user
#configuración del buscador
def search_data(query):
  posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()
  return posts
#index
@bp.route('/', methods = ['GET', 'POST'])
def index():
  posts = Post.query.all()
  if request.method == 'POST':
    query = request.form.get('search')
    posts = search_data(query)
    value = 'hidden'
    return render_template('index.html', posts = posts, get_user = get_user, value = value)
  return render_template('index.html', posts = posts, get_user = get_user)
#mostrar el blog
@bp.route('/blog/<url>')
def blog(url):
  post = Post.query.filter_by(url = url).first()
  return render_template('blog.html', post = post, get_user = get_user)