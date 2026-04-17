from flask import render_template, request, redirect, url_for, flash
from . import ins_bp
from models import db, Alumnos, Curso
import forms

@ins_bp.route("/inscribir", methods=["GET", "POST"])
def inscribir_alumno():
    form = forms.InscripcionForm(request.form)
    
    # Llenamos las listas desplegables directo de la BD
    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno}") for a in Alumnos.query.all()]
    form.curso_id.choices = [(c.id, c.nombre) for c in Curso.query.all()]

    if request.method == "POST" and form.validate():
        # Jalamos los objetos reales de la base de datos
        alumno = Alumnos.query.get(form.alumno_id.data)
        curso = Curso.query.get(form.curso_id.data)
        
        # AQUÍ ESTÁ EL .APPEND (Validamos que no esté inscrito ya)
        if alumno not in curso.alumnos:
            curso.alumnos.append(alumno)
            db.session.commit()
            flash(f"¡{alumno.nombre} inscrito correctamente en {curso.nombre}!", "success")
        else:
            flash("El alumno ya estaba inscrito en este curso.", "error")
            
        return redirect(url_for('inscripciones.inscribir_alumno'))
        
    return render_template("inscribir.html", form=form)