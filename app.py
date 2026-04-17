from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
import forms

# <-- IMPORTANTE: Agregamos Curso e Inscripcion para que db.create_all() las detecte
from models import db, Alumnos, Maestros, Curso, Inscripcion
from forms import UserForm, MaestroForm

# 1. IMPORTAMOS LOS BLUEPRINTS (Módulos)
from maestros import maestros_bp
from alumnos import alumnos_bp 
from cursos import cursos_bp           # <-- NUEVO: Importamos el de cursos
from inscripciones import ins_bp       # <-- NUEVO: Importamos el de inscripciones

# 2. INICIALIZAMOS LA APP 
app = Flask(__name__)  
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

# 3. CONECTAMOS LOS MÓDULOS A TU APP PRINCIPAL
app.register_blueprint(maestros_bp)
app.register_blueprint(alumnos_bp) 
app.register_blueprint(cursos_bp)      # <-- NUEVO: Lo registramos en la app
app.register_blueprint(ins_bp)         # <-- NUEVO: Lo registramos en la app

# ==========================================
# RUTAS PRINCIPALES
# ==========================================

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    # Menú principal (pantalla genérica de bienvenida)
    return render_template("index.html")

# ==========================================
# INICIO DE LA APLICACIÓN
# ==========================================
if __name__ == "__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)