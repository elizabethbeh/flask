from flask import Blueprint, request, jsonify, session, redirect, url_for
from flask_jwt_extended import create_access_token
from flask_cors import CORS

auth_bp = Blueprint("auth", __name__)  # Blueprint para autenticación
CORS(auth_bp)

# Usuarios de prueba
users = {
    "admin": {"password": "1234", "role": "admin"},
    "user": {"password": "5678", "role": "user"}
}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.form  # Recibir datos del formulario en HTML
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and user["password"] == password:
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        session["jwt_token"] = access_token  # Guardar token en sesión
        return redirect(url_for("routes.protected"))  # Redirigir a la ruta protegida

    return jsonify({"error": "Credenciales inválidas"}), 401
