from flask_sqlalchemy import SQLAlchemy #ORM
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    _tablename_ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apaterno = db.Column(db.String(50), nullable=False)
    amaterno = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    edad = db.Column(db.Date, nullable=False)

class Profesores(db.Model):
    __tablename__ = 'profesores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apaterno = db.Column(db.String(50), nullable=False)
    amaterno = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    materia = db.Column(db.String(100), nullable=False) # Campo extra de ejemplo