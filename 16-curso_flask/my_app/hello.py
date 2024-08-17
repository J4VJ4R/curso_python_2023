from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
app = Flask(__name__)
app.config.from_mapping(
  SECRET_KEY = 'DEV'
)

#Filtros personalizados
@app.add_template_filter
def today(date):
  return date.strftime('%d-%m-%Y')

from datetime import datetime

@app.route('/')
def index():
  print(url_for('index'))
  print(url_for('hello', name = 'Alex'))
  print(url_for('code', code = 'print("hola")'))
  name = None
  date = datetime.now()
  friends = ['Alex', 'Berta', 'Camilo', 'Camila']
  return render_template('index.html',
                         name = name,
                         friends = friends,
                         date = date)
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name = None, age = None, email = None):
  my_data = {
    'name': name,
    'age': age,
    'email': email
  }
  return render_template('hello.html', my_data = my_data)
  
from markupsafe import escape

@app.route('/code/<path:code>')
def code(code):
  return f'<code>{escape(code)}</code>'
# Crear form con formwtf
class RegisterForm(FlaskForm):
  username = StringField("Nombre de usuario: ", validators=[DataRequired(), Length(min=4, max=25)])
  password = PasswordField("Password: ", validators=[DataRequired(), Length(min=4, max=40)])
  submit = SubmitField("Registrar: ")
# registrar usuarios
@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    return f"Nombre de usuario: {username} Password: {password}"
  # if request.method == 'POST':
  #   username = request.form['username']
  #   password = request.form['password']
  #   if len(username) >= 4 and len(username) <= 25 and len(password) >= 4 and len(password) <= 40:
  #     return f'Nombre de usuario: {username} Contraseña: {password}'
  #   else:
  #     error = """
  #       Nombre de usuario debe tener entre 4 y 25 caracteres y la contraseña debe
  #       tener entre 4 y 40 caracteres
  #     """
  #   return render_template('auth/register.html', form = form, error = error)

  return render_template('auth/register.html', form = form)