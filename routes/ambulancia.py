from flask import Blueprint, jsonify, request

# Entities
from models.entities.Chofer import Chofer
from models.entities.Paramedico import Paramedico
from models.entities.Ambulancia import Ambulancia

# Models
from models.paramedicoModel import ParamedicoModel
from models.choferModel import ChoferModel
from models.ambulanciaModel import AmbulanciaModel

AmbulanciaApi = Blueprint("ambulancia_blueprint", __name__)


@AmbulanciaApi.route("/")
def get_ambulancias():
    try:
        ambulancias = AmbulanciaModel.get_ambulancia()
        return jsonify(ambulancias)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AmbulanciaApi.route("/<id>")
def get_ambulanciaxId(id):
    try:
        if id:
            chofer = ChoferModel.get_chofer(id)
            return (
                jsonify(
                    {
                        "chofere": chofer,
                        "message": "OK",
                    }
                ),
                200,
            )
        return jsonify({"message": "falta el valor ID chofer"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500