from wtforms import Form
from wtforms import StringField, IntegerField, EmailField, PasswordField
from wtforms import validators

class UserForm(Form):
    id=IntegerField("ID")
    nombre=StringField('Nombre')
    apaterno=StringField('Apaterno')
    amaterno=StringField('Amaterno')
    edad=IntegerField("Edad")
    correo=EmailField('Correo')

# --- NUEVO FORMULARIO PARA MAESTROS ---
class MaestroForm(Form):
    matricula = IntegerField("Matrícula")
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    especialidad = StringField('Especialidad')
    email = EmailField('Correo')