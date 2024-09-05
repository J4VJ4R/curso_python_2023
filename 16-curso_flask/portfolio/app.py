from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from language import es, en

app = Flask(__name__)

#configuración de email
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'be9ac5ab589331'
app.config['MAIL_PASSWORD'] = '5c0bc09fd5e9eb'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Configuración de email usando el servidor SMTP de cPanel
# app.config['MAIL_SERVER'] = 'mail.spacecode.com.co'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'info@spacecode.com.co'
# app.config['MAIL_PASSWORD'] = 'tu_password'  # Sustituye con la contraseña de tu cuenta de correo
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True  # Debe ser True ya que el puerto 465 es SSL

mail = Mail(app)

#normal index
@app.route('/')
def index():
  return indexlang('es')
#index with language
@app.route('/<lang>')
def indexlang(lang):
  messages = get_language(lang)
  return render_template('index.html', messages = messages, lang = lang)
#for change language
def get_language(lang):
  if lang == "es":
    return es.messages
  elif lang == "en":
    return en.messages
  else:
    return es.messages


@app.route('/email', methods = ['GET', 'POST'])
def send_mail():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    msg = Message(
      'Hola SpaceCode, tiene un nuevo mensajes desde la web: ',
      body = f'Nombre: {name} \n Correo: <{email}> \n\n Escribió: \n\n {message}',
      sender = email,
      recipients=['info@spacecode.com.co']
    )
    mail.send(msg)
    return render_template('send-email.html')
  return redirect(url_for('index'))