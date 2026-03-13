from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apaterno = db.Column(db.String(50), nullable=False)
    amaterno = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    edad = db.Column(db.Date, nullable=False)

# --- NUEVO MODELO DE MAESTROS ---
class Maestros(db.Model):
    __tablename__ = 'maestros'
    matricula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    especialidad = db.Column(db.String(50))
    email = db.Column(db.String(50))
    cursos = db.relationship('Curso', back_populates='maestro')