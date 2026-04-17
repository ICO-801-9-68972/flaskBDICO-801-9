from flask import render_template, request, redirect, url_for, flash
from . import cursos_bp 
from models import db, Curso, Maestros, Alumnos 
import forms

@cursos_bp.route("/cursos")
def lista_cursos():
    todos_cursos = Curso.query.all()
    return render_template("cursos/cursos.html", cursos=todos_cursos)

@cursos_bp.route("/crear_curso", methods=["GET", "POST"])
def crear_curso():
    form = forms.CursoForm(request.form)
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
    
    if request.method == "POST" and form.validate():
        nuevo_curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        flash("Curso creado correctamente", "success")
        return redirect(url_for('cursos.lista_cursos'))
        
    return render_template("cursos/crear_cursos.html", form=form)

# --- NUEVA RUTA: PARA REASIGNAR (MODIFICAR) EL CURSO ---
@cursos_bp.route("/modificar_curso/<int:id>", methods=["GET", "POST"])
def modificar(id):
    curso = Curso.query.get_or_404(id)
    # Llenamos el form con los datos del curso actual
    form = forms.CursoForm(obj=curso)
    # Cargamos los maestros disponibles
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]
    
    if request.method == "POST" and form.validate():
        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data
        
        db.session.commit()
        flash("Curso reasignado correctamente", "success")
        return redirect(url_for('cursos.lista_cursos'))
        
    return render_template("cursos/crear_cursos.html", form=form, curso=curso)

# --- NUEVA RUTA: PARA BORRAR EL CURSO "AHÍ MISMO" ---
@cursos_bp.route("/eliminar_curso_rapido/<int:id_curso>/<int:id_maestro>", methods=["POST"])
def eliminar_rapido(id_curso, id_maestro):
    curso = Curso.query.get_or_404(id_curso)
    db.session.delete(curso)
    db.session.commit()
    flash(f"Curso '{curso.nombre}' eliminado correctamente.", "success")
    # Regresamos a la pantalla de eliminar del maestro para que se refresque
    return redirect(url_for('maestros.eliminar', id=id_maestro))

@cursos_bp.route("/alumnos_en_curso")
def alumnos_en_curso():
    id_curso = request.args.get("id")
    if not id_curso:
        return redirect(url_for('cursos.lista_cursos'))
        
    curso = Curso.query.get_or_404(id_curso)
    return render_template("cursos/alumnos_inscritos.html", curso=curso)