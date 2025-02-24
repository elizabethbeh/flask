from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS']='Content-Type'

# Clave secreta para firmar los tokens (usa una variable de entorno en producción)
app.config["SECRET_KEY"] = "super"  
app.config["JWT_SECRET_KEY"] = "supersecreto"
app.config["JWT_TOKEN_LOCATION"] = ['headers']  
jwt = JWTManager(app)

# Usuarios de ejemplo (en una base de datos real, esto vendría de ahí)
users = {
    "admin": {"password": "1234", "role": "admin"},
    "user": {"password": "5678", "role": "user"}
}

# Ruta para autenticarse y obtener un JWT
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Verificar credenciales
    user = users.get(username)
    if user and user["password"] == password:
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Credenciales inválidas"}), 401

# Ruta protegida con JWT
@app.route("/protected", methods=["POST"])
@jwt_required()
def protected():
    print('pasa para aca1')
    current_user = get_jwt_identity()  # Obtiene la identidad del usuario autenticado
    print('pasa para aca')
    return jsonify({"message": "Bienvenido!"})

# Ruta protegida para obtener usuario específico
@app.route("/users/<user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Acceso denegado"}), 403

    user = {"id": user_id, "name": "test", "telefono": "999-666-333"}
    return jsonify(user), 200

if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=5000)
