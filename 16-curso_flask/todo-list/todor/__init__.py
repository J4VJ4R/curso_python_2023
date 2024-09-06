from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from language import es, en
from todor.language import get_language
#Crear extensión
db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  #configuración del proyecto
  app.config.from_mapping(
    DEBUG = False,
    SECRET_KEY = 'devtodo*',
    SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db",
    LANG = 'es'
  )
  #Inicio de la conexión en db
  db.init_app(app)
  #Registrar bluprint
  from . import todo
  app.register_blueprint(todo.bp)
  from . import auth
  app.register_blueprint(auth.bp)
  #inside index normal index
  @app.route('/')
  def index():
    return indexlang('es')
  #index with language
  @app.route('/<lang>')
  def indexlang(lang):
    messages = get_language(lang)
    return render_template('index.html', messages = messages, lang = lang)
  #migración de modelos
  with app.app_context():
    db.create_all()
  return app