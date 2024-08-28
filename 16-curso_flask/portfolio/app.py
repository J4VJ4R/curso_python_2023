from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

#configuración de email
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'be9ac5ab589331'
app.config['MAIL_PASSWORD'] = '5c0bc09fd5e9eb'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
@app.route('/')
def index():
  return render_template('index.html')

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