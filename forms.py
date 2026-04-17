from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, EmailField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class UserForm(Form):
    id = IntegerField("ID")  # Este es el nombre que Jinja2 buscará
    nombre = StringField("Nombre")
    apaterno = StringField("APaterno")
    amaterno = StringField("AMaterno")
    edad = IntegerField("Edad")
    correo = EmailField("Correo")

class MaestroForm(FlaskForm):
    id = IntegerField("Matricula")
    nombre = StringField("Nombre")
    apellidos = StringField("Apellidos")
    especialidad = StringField("Especialidad")
    email = EmailField("Email")

# --- LO NUEVO PARA LOS CURSOS E INSCRIPCIONES ---

class CursoForm(FlaskForm):
    id = IntegerField("ID")
    nombre = StringField("Nombre del Curso", validators=[DataRequired()])
    descripcion = TextAreaField("Descripción")
    # coerce=int asegura que el ID del maestro se guarde como número y no como texto
    maestro_id = SelectField("Maestro Asignado", coerce=int, validators=[DataRequired()])

class InscripcionForm(FlaskForm):
    # SelectFields para que en la vista te salga una lista desplegable con los nombres
    alumno_id = SelectField("Seleccionar Alumno", coerce=int, validators=[DataRequired()])
    curso_id = SelectField("Seleccionar Curso", coerce=int, validators=[DataRequired()])