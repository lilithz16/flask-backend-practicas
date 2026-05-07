from flask import Flask, jsonify, request
from flask_cors import CORS

from services.validation_service import validar_datos_candidato

app = Flask(__name__)

CORS(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "API running",
        "message": "Bienvenida a mi API de prácticas"
    }), 200


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "success": True,
        "message": "Backend funcionando correctamente"
    }), 200


@app.route("/api/solicitud", methods=["POST"])
def recibir_solicitud():
    datos_candidato = {
        "nombre": request.form.get("nombre"),
        "apellidos": request.form.get("apellidos"),
        "email": request.form.get("email"),
        "telefono": request.form.get("telefono"),
        "puesto": request.form.get("puesto"),
        "jornada": request.form.get("jornada"),
        "ubicacion": request.form.get("ubicacion"),
        "mensaje": request.form.get("mensaje"),
        "privacidad": request.form.get("privacidad")
    }

    es_valido, mensaje = validar_datos_candidato(datos_candidato)

    if not es_valido:
        return jsonify({
            "success": False,
            "message": mensaje
        }), 400

    cv = request.files.get("cv")

    if cv is None or cv.filename == "":
        return jsonify({
            "success": False,
            "message": "Debe adjuntar un CV."
        }), 400

    return jsonify({
        "success": True,
        "message": "Datos y CV recibidos correctamente",
        "datos_recibidos": datos_candidato,
        "archivo_recibido": cv.filename
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)