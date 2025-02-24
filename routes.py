from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

users_bp = Blueprint("users", __name__)

# Ruta DELETE protegida con JWT
@users_bp.route('/users/<user_id>', methods=['DELETE'])
@jwt_required()  # 🔐 Requiere un JWT válido
def delete_user(user_id):
    current_user = get_jwt_identity()  # Obtiene el usuario autenticado
    return jsonify({"message": f"Usuario {user_id} eliminado por {current_user['username']}"}), 200
