from flask import Flask

#creando la aplicación
def create_app():
  app = Flask(__name__)
  #archivo de configuración
  app.config.from_object('config.Config')
  #registrar vistas
  from blog import home
  app.register_blueprint(home.bp)
  from blog import auth
  app.register_blueprint(auth.bp)
  from blog import post
  app.register_blueprint(post.bp)
  return app
 
