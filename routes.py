from flask import Blueprint, jsonify, render_template, session, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity

routes_bp = Blueprint("routes", __name__)  # Blueprint de rutas

@routes_bp.route("/protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    
    return render_template("protected.html", user=current_user)

