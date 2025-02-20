from flask import Blueprint, request, jsonify
from MongoDB.Services.ClienteService import *
from Cassandra.Session import sesiones 
from MongoDB.Services.ProductoService import *
from MongoDB.Services.SolicitudService import *
ultima_sesion_GET = Blueprint("ultima_sesion", __name__)  # Se usa un Blueprint en vez de crear otra app

@ultima_sesion_GET.route("/session/ultima", methods=["GET"])
def carrito_en_ultima_sesion_GET():
    data = request.json
    respuesta={}
    try:
            nombre_cliente = data.get("nombre")
            contraseña_cliente=data.get("contraseña")
            cliente=obtener_cliente_nomb_y_contra(nombre_cliente,contraseña_cliente)
            
            productos_de_session=[]
            cantidad_de_productos=[]
            print(f"session anterior: {sesiones.obtener_session_por_id_sesion(sesiones.ultima_sesion_de_cliente(cliente.get("_id")))}")
            ultima_solicitud=sesiones.obtener_session_por_id_sesion(sesiones.ultima_solicitud(cliente.get("_id")))
            print(ultima_solicitud)
            productos=ultima_solicitud.get("productos")
            for prod in productos:
                  productos_de_session.append(obtener_producto_por_id(prod))
            cantidades=ultima_solicitud.get("cantidad")
            for cant in cantidades:
                  cantidad_de_productos.append(cant)
            
            respuesta["productos":productos_de_session,"cantidades":cantidad_de_productos]


            return jsonify({"respuesta":f" el carrito de la última session registrada contiene {respuesta}" }),200
    except Exception as e:
          print(f"no se pudo cerrar la sesion del usuario {e}")
          return jsonify({"respuesta":f" no se pudo obtener carrito de la última session {e}" }),200