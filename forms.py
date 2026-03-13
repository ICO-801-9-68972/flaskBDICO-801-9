from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
# IMPORTANTE: Agregar Maestros aquí
from models import db, Alumnos, Maestros 
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf = CSRFProtect(app)

# ... (Tus rutas de / y /usuarios se mantienen igual) ...

# --- NUEVAS RUTAS PARA MAESTROS ---
@app.route("/maestros", methods=["GET", "POST"])
def maestros():
    create_maestro = forms.MaestroForm(request.form)
    # select * from maestros
    maestro = Maestros.query.all()
    return render_template("maestros.html", form=create_maestro, maestro=maestro)

@app.route("/datos_maestros", methods=["GET", "POST"])
def datos_maestros():
    mat = 0
    nom = ''
    ape = ''
    esp = ''
    email = ''
    maestros_clas = forms.MaestroForm(request.form)
    
    if request.method == 'POST':
        mat = maestros_clas.matricula.data
        nom = maestros_clas.nombre.data
        ape = maestros_clas.apellidos.data
        esp = maestros_clas.especialidad.data
        email = maestros_clas.email.data
    
    return render_template('datos_maestros.html', form=maestros_clas, mat=mat, nom=nom, ape=ape, esp=esp, email=email)

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()