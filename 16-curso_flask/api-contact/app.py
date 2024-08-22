from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#creamos la aplicación
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)

#crear modelo de la base de datos
class Contact(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), nullable=False)
  phone = db.Column(db.String(10), nullable=False)

  def serialize(self):
    return {
      'id':self.id,
      'name':self.name,
      'email':self.email,
      'phone':self.phone
    }
#crea automáticamente las tablas en las bases de datos
with app.app_context():
  db.create_all()
#crear rutas
@app.route('/contacts', methods = ['GET'])
def get_contacts():
  contacts = Contact.query.all()
  return jsonify({'contacts': [contact.serialize() for contact in contacts]})

@app.route('/contacts', methods = ['POST'])
def create_contacts():
  data = request.get_json()
  contact = Contact(name = data['name'],
                    email = data['email'],
                    phone = data['phone'])
  db.session.add(contact)
  db.session.commit()
  return jsonify({'message':'Se creó un contacto', 'contact': contact.serialize()}), 201

#obtener un solo elemento
@app.route('/contacts/<int:id>', methods = ['GET'])
def get_contact(id):
  contact = Contact.query.get(id)
  if not contact:
    return jsonify({'message':'Contacto no encontrado'}), 404
  return jsonify(contact.serialize())
#actualizar datos por id
@app.route('/contacts/<int:id>', methods = ['PUT', 'PATCH'])
def update_contact(id):
  contact = Contact.query.get_or_404(id)
  #recibe los datos de la petición json
  data = request.get_json()
  #cambio de los datos
  if 'name' in data:
    contact.name = data['name']
  if 'email' in data:
    contact.email = data['email']
  if 'phone' in data:
    contact.phone = data['phone']
  #se guarda los datos en la base de datos
  db.session.commit()
  #retorna un mensaje del cambio con el objetio json
  return jsonify({'message':'Contacto actualizado con éxito', 'contact':contact.serialize()}), 201
#eliminar datos
@app.route('/contacts/<int:id>', methods = ['DELETE'])
def delete_contact(id):
  contact = Contact.query.get(id)
  if not contact:
    return jsonify({'message':'Contacto no encontrado'}), 404
  #borrar dato
  db.session.delete(contact)
  db.session.commit()
  return jsonify({'message':'Contacto eliminado con éxito'})