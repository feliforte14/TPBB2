from flask import Blueprint, request, jsonify
from MongoDB.Services.ClienteService import *
from Cassandra.Session import sesiones 
cerrar_sesion_POST = Blueprint("cerrar_session", __name__)  # Se usa un Blueprint en vez de crear otra app

@cerrar_sesion_POST.route("/session/cerrar", methods=["post"])
def pedido_POST():
    data = request.json
    
    try:
            nombre_cliente = data.get("nombre")
            contraseña_cliente=data.get("contraseña")
            cliente=obtener_cliente_nomb_y_contra(nombre_cliente,contraseña_cliente)
            ultima_sesion=sesiones.cerrar_session(cliente.get("_id"))
            return jsonify({"respuesta":f" se cerró la última sesion {str(ultima_sesion)}" }),200
    except Exception as e:
          print(f"no se pudo cerrar la sesion del usuario {e}")