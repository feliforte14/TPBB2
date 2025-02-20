from flask import Blueprint, request, jsonify
from urllib.parse import quote, unquote
from MongoDB.Models.Solicitud import Solicitud
from MongoDB.Services.SolicitudService import *
from Cassandra.Session import sesiones
from MongoDB.Services.ClienteService import *
from MongoDB.Services.EstadoSolicitudService import *
from MongoDB.Services.ProductoService import *

iniciar_sesion_POST = Blueprint("iniciar_session", __name__)  # Se usa un Blueprint en vez de crear otra app

@iniciar_sesion_POST.route("/session/iniciar", methods=["post"])
def pedido_POST():
    data = request.json
      #busca al cliente
    try:
        try:
            nombre_cliente = data.get("nombre")
            contraseña_cliente=data.get("contraseña")
            cliente=obtener_cliente_nomb_y_contra(nombre_cliente,contraseña_cliente)
        except Exception as e:
            return jsonify({"no se se encontró cliente": str(e)}), 500            

        resultado=    sesiones.iniciar_session(cliente.get("_id"))
        return jsonify(resultado),200
    except Exception as e:
        return jsonify({"no se se inició la session": str(e)}), 500