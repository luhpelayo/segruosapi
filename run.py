from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from decouple import config
from flask_cors import CORS

from routes import phone
from routes import enfermedad
from routes import alergia
from routes import persona
from routes import hospital
from routes import siniestro

from controllers.AlergiaController import alergiaweb
from controllers.EnfermedadController import enfermedadweb
from controllers.PersonaController import personaweb

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config["SECRET_KEY"] = config("SECRET_KEY")
csrf.init_app(app)
# CORS(app, resources={"*": {"origins": "http://localhost:9300"}})


@app.route("/")
def index():
    return render_template("login.html")


def page_not_found(error):
    return render_template("404.html"), 404


# Blueprints App Web
app.register_blueprint(alergiaweb, url_prefix="/alergia")
app.register_blueprint(enfermedadweb, url_prefix="/enfermedad")
app.register_blueprint(personaweb, url_prefix="/paciente")

# Blueprints Api Rest
app.register_blueprint(phone.PhoneApi, url_prefix="/api/phone")
app.register_blueprint(alergia.AlergiaApi, url_prefix="/api/alergia")
app.register_blueprint(enfermedad.EnfermedadApi, url_prefix="/api/enfermedad")
app.register_blueprint(hospital.HospitalApi, url_prefix="/api/hospital")
app.register_blueprint(siniestro.SiniestroApi, url_prefix="/api/siniestro")
app.register_blueprint(persona.PersonaApi, url_prefix="/api/persona")
# Error handlers
app.register_error_handler(404, page_not_found)
# inits

if __name__ == "__main__":
    app.run(debug=True)
