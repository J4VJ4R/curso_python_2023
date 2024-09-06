from flask import Blueprint, render_template, request, g, redirect, url_for
from todor.auth import login_required
from .models import Todo, User
from todor import db
from todor.language import get_language
bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/list/<lang>')
@login_required
def index(lang):
  messages = get_language(lang)
  todos = Todo.query.all()
  return render_template('todo/index.html', todos = todos, messages = messages, lang = lang)

@bp.route('/create/<lang>', methods = ('GET', 'POST'))
@login_required
def create(lang):
  messages = get_language(lang)
  if request.method == 'POST':
    title = request.form['title']
    description = request.form['description']
    #creando tarea
    todo = Todo(g.user.id, title, description)
    #enviando tarea a base de datos
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('todo.index', lang = lang))
  return render_template('todo/create.html', messages = messages, lang = lang)

#obtener tarea
def get_todo(id):
  todo = Todo.query.get_or_404(id)
  return todo
#actualizar datos
@bp.route('/update/<int:id>/<lang>', methods = ('GET', 'POST'))
@login_required
def update(id, lang):
  messages = get_language(lang)
  todo = get_todo(id)
  if request.method == 'POST':
    todo.title = request.form['title']
    todo.desc = request.form['description']
    todo.state = True if request.form.get('state') == 'on' else False
    #efectuar cambios
    db.session.commit()
    return redirect(url_for('todo.index', messages = messages, lang = lang))
  return render_template('todo/update.html', todo = todo, messages = messages)
#eliminar datos
@bp.route('/delete/<int:id>/<lang>')
@login_required
def delete(id, lang):
  messages = get_language(lang)
  todo = get_todo(id)
  if todo:
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index', lang = lang))
  else:
    return redirect(url_for('todo.index', lang = lang))

  
    