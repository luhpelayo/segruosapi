from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import datetime
import random
import string
import cloudinary
from cloudinary import uploader, api
from cloudinary.utils import cloudinary_url
from decouple import config


# Entities
from models.entities.Persona import Persona

# Models
from models.personaModel import PersonaModel

PersonaApi = Blueprint("prna_blueprint", __name__)

@PersonaApi.route('/add',methods=['POST'])
def add_persona():
    try:
        if request.method=='POST':
            data = request.json
            if data:
                _ci = data['ci']
                _nombre = data['nombres']
                _apellido = data['apellidos']
                _fecha = data['fecha_nacimiento']
                _direccion = data['direccion']  if data['direccion'] else ''
                _genero = data['genero']
                _estado_civil = data['estado_civil']                
                new_persona = Persona(_ci,_nombre,_apellido,_fecha,None,None,_direccion,_genero,_estado_civil)
                new_ci = PersonaModel.add_persona(new_persona)
                return jsonify({'ci_persona':new_ci}), 200                
        return jsonify({'message':'Metodo http diferente de Post'}), 404 
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    
@PersonaApi.route("/upload/<ci>", methods=["POST"])
def upload_perfil(ci):
    try:
        if ci:
            if request.method == "POST":
                file = request.files["photo"]
                if file:
                    cloudinary.config(
                        cloud_name=config("CLOUD_NAME"),
                        api_key=config("API_KEY"),
                        api_secret=config("API_SECRET"),
                    )
                    now = datetime.datetime.now()
                    random_str = "".join(
                        random.choices(string.ascii_letters + string.digits, k=5)
                    )
                    unique_str = now.strftime("%Y%m%d_%H%M%S_") + random_str
                    foto_name = secure_filename(str(unique_str))
                    upload_result = cloudinary.uploader.upload(
                        file, public_id="photo/" + foto_name
                    )
                    foto_url = upload_result["secure_url"]
                    foto_name = foto_name + "." + upload_result["format"]
                    per = Persona(
                        ci, None, None, None, foto_url, foto_name, None, None, None
                    )
                    PersonaModel.upload_photo(per)
                    return jsonify({"message": "Imagen guardado correctamente"}), 200
                return jsonify({"message": "No se ha podido guardar el Imagen"}), 400
            else:
                return jsonify({"message": "Metodo no permitido"}), 400
        else:
            return jsonify({"message": "Metodo no permitido"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
