from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
#from routes import users_bp  #importo el Bluepoint de rutas

app = Flask(__name__)

# Clave secreta para firmar los tokens JWT
app.config["JWT_SECRET_KEY"] = "supersecreto"
jwt = JWTManager(app)

# Registrar el Blueprint de rutas
#app.register_blueprint(users_bp)

@app.route("/")
def home():
    return "¡Hola, Flask en Windows con virtualenv!"

#Defino la ruta /users y le paso el parametro user
@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id": user_id, "name": "test", "telefono": "999-666-333"}
    # /users/2654?query=query_test
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
        data = request.get_json()
        data['status']='user created'
        return jsonify(data), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    update_user = {"id": user_id, "name": data.get("name", "Nombre no especificado"), "telefono": data.get("telefono", "Teléfono no especificado"), "status": "user updated"}
    return jsonify(update_user), 200



@app.route('/users/<user_id>', methods=['DELETE'])
#@jwt_required()
def delete_user(user_id):
    current_user = get_jwt_identity()
    response = {
        'id': user_id,
        'status': 'user deleted'
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)