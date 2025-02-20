from flask import Blueprint, request, jsonify
from urllib.parse import quote, unquote
from MongoDB.Models.Solicitud import Solicitud
from MongoDB.Services.SolicitudService import *
from Cassandra.Session import sesiones
from MongoDB.Services.ClienteService import *
from MongoDB.Services.EstadoSolicitudService import *
from MongoDB.Services.ProductoService import *

hacer_pedido_post_blue = Blueprint("hacer pedido", __name__)  # Se usa un Blueprint en vez de crear otra app

@hacer_pedido_post_blue.route("/pedidos/nuevo", methods=["POST"])
def pedido_POST():
    data = request.json
      #busca al cliente
    nombre_cliente = data.get("nombre")
    contraseña_cliente=data.get("contraseña")
    try: 
            cliente=obtener_cliente_nomb_y_contra(nombre_cliente,contraseña_cliente)

    except Exception as e:
            return jsonify({"no se encontró cliente": str(e)}), 500
    try:
        cliente_solicitud= sesiones.ultima_solicitud(cliente.get("_id"))
        
        resultado=        carrito_a_pedido(cliente.get("_id"),cliente_solicitud)
        return jsonify(resultado),200
    except Exception as e:
        return jsonify({"no se se realizó el pedido": str(e)}), 500