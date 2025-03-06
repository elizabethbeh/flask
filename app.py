from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from auth import auth_bp
from routes import routes_bp

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "super"  
app.config["JWT_SECRET_KEY"] = "supersecreto"
#app.config["JWT_TOKEN_LOCATION"] = ["headers"]  # Usar headers en vez de cookies
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]  # Usar cookies en vez de headers
app.config["SESSION_TYPE"] = "filesystem"  # Para manejar sesiones

jwt = JWTManager(app)

# Registrar Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)

# Página de inicio con login
@app.route("/")
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
