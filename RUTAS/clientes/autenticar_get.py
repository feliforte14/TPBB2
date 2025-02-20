from flask import Blueprint, request, jsonify
from MongoDB.Services.ClienteService import *
autenticar_blue = Blueprint("categorias", __name__)  # Se usa un Blueprint en vez de crear otra app

@autenticar_blue.route("/autenticar", methods=["get"])
def autenticar_GET():
    try:
        data = request.json
        nombre = data.get("nombre")
        contraseña = data.get("contraseña")

        id_cliente:autenticar_cliente(nombre,contraseña)
        


    except Exception as e:
        return jsonify({"error": str(e)}), 500