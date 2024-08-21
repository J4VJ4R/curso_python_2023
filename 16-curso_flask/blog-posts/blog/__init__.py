from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#creando la aplicación
def create_app():
  app = Flask(__name__)
  #archivo de configuración
  app.config.from_object('config.Config')
  #inicio de base de datos
  db.init_app(app)
  #configurar idioma
  import locale
  locale.setlocale(locale.LC_ALL, 'es_ES')
  #registrar vistas
  from blog import home
  app.register_blueprint(home.bp)
  from blog import auth
  app.register_blueprint(auth.bp)
  from blog import post
  app.register_blueprint(post.bp)
  #agrega los modelos a la base de datos
  from .models import User, Post
  with app.app_context():
    db.create_all()
  return app
 
