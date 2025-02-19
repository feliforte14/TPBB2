from flask import Flask, request, jsonify

from RUTAS import api_blueprint
app = Flask(__name__)

# Registrar rutas desde otro archivo
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5000)