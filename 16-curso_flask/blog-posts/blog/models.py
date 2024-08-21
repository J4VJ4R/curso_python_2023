from blog import db
from datetime import datetime

#crear tabla de usuarios
class User(db.Model):
  #nombre de la tabla
  __tablename__ = 'users' #indica el nuevo nombre de la tabla por si se quiere cambiar (User)
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), nullable = False)
  email = db.Column(db.String(150), unique=True, nullable = False)
  password = db.Column(db.Text, nullable=False)
  img = db.Column(db.String(200))
  #se crea el constructor
  def __init__(self, username, email, password, img = None):
    """
    Inicializa una nueva instancia de la clase `User`.

    Este método constructor establece los atributos básicos para una instancia de `User`, 
    incluyendo el nombre de usuario, el correo electrónico, la contraseña y, opcionalmente, una foto.

    Args:
        username (str): El nombre de usuario que identifica al usuario.
        email (str): La dirección de correo electrónico asociada al usuario.
        password (str): La contraseña del usuario. Debe ser almacenada de manera segura.
        img (str, optional): La ruta o URL de la foto del usuario. Este argumento es opcional 
        y tiene un valor predeterminado de `None`.
    """
    self.username = username
    self.email = email
    self.password = password
    self.img = img
  def __repr__(self):
    """
    Devuelve una representación legible del objeto `User`.

    Este método especial se utiliza para definir cómo se debe representar 
    una instancia de la clase `User` cuando se imprime o se inspecciona. 
    La representación incluye el nombre de usuario de la instancia.

    Returns:
        str: Una cadena en el formato "User: '<username>'", donde 
        <username> es el nombre de usuario de la instancia.
    """
    return f"User: '{self.username}'"
#nueva clase para publicaciones de posts
class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key = True)
  author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  url = db.Column(db.String(100), unique = True, nullable = False)
  title = db.Column(db.String(100), nullable = False)
  info = db.Column(db.Text)
  content = db.Column(db.Text)
  created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

  def __init__(self, author, url, title, info, content, created):
    self.author = author
    self.url = url
    self.title = title
    self.info = info
    self.content = content
  
  def __repr__(self):
    return f'Post: {self.title}'