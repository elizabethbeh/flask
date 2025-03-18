from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from auth import auth_bp
from routes import routes_bp

from flask_jwt_extended import set_access_cookies

app = Flask(__name__)
CORS(app)

app.config["JWT_TOKEN_LOCATION"] = ["cookies"]  # Habilitar autenticación por cookies
app.config["JWT_COOKIE_SECURE"] = False  # Debe ser True si usas HTTPS
app.config["JWT_ACCESS_COOKIE_NAME"] = "access_token_cookie"  # Nombre de la cookie
app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # Desactiva protección CSRF (solo para pruebas)

app.config["SECRET_KEY"] = "superclave"  # Para sesiones de Flask
app.config["JWT_SECRET_KEY"] = "supersecreto"  # Para firmar tokens JWT

jwt = JWTManager(app)

# Registrar Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)

# Página de inicio con login
@app.route("/")
def home():
    return render_template("login.html")

def hello():
    user_ip = request.remote_addr
    return 'Hello World Platzi, tu IP es {}'.format(user_ip)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


