from flask_login import login_required
from flask import Blueprint
from flask import (
    render_template,
    redirect,
    request,
    flash,
)
from models.entities.Enfermedad import Enfermedad
from models.enfermedadModel import EnfermedadModel

enfermedadweb = Blueprint(
    "enfermedad_bp", __name__, template_folder="templates/enfermedad"
)


@enfermedadweb.route("/")
@login_required
def index():
    enfermedadList = EnfermedadModel.get_enfermedads()
    return render_template("/enfermedad/index.html", enfermedads=enfermedadList)


@enfermedadweb.route("/create", methods=["POST"])
@login_required
def create():
    if request.method == "POST":
        try:
            _nombre = request.form.get("txtNombre")
            enfermedad = Enfermedad(None, _nombre)
            EnfermedadModel.add_enfermedad(enfermedad)
            flash("Enfermedad Agregada successfully")
            return redirect("/enfermedad")
        except Exception as e:
            flash(e.args[1])
            return redirect("/enfermedad")


@enfermedadweb.route("/update/<id>", methods=["GET", "POST"])
@login_required
def update(id):
    if request.method == "POST":
        try:
            _nombre = request.form.get("txtNombre")
            enfermedad = Enfermedad(id, _nombre)
            EnfermedadModel.update_enfermedad(enfermedad)
            flash("Enfermedad Updated Successfully")
            return redirect("/enfermedad")
        except Exception as e:
            flash(e.args[1])
            return redirect("/enfermedad")


@enfermedadweb.route("/delete/<id>", methods=["GET", "POST"])
@login_required
def delete(id):
    if request.method == "POST":
        enfermedad = Enfermedad(id, "Elimina")
        try:
            EnfermedadModel.delete_enfermedad(enfermedad)
            flash("Alergia Eliminada Successfully")
            return redirect("/enfermedad")
        except Exception as e:
            flash(e.args[1])
            return redirect("/enfermedad")
