from flask import Flask, jsonify
from flask_cors import CORS

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)