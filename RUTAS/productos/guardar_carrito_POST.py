from flask import Blueprint, request, jsonify
from urllib.parse import quote, unquote
from MongoDB.Models.Solicitud import Solicitud
from MongoDB.Services.SolicitudService import *
from Cassandra.Session import sesiones
from MongoDB.Services.ClienteService import *
from MongoDB.Services.EstadoSolicitudService import *
from MongoDB.Services.ProductoService import *

carrito_post_blue = Blueprint("carrito", __name__)  # Se usa un Blueprint en vez de crear otra app

@carrito_post_blue.route("/carrito", methods=["post"])
def carrito_POST():
    try:
        
        data = request.json
        #busca al cliente
        nombre_cliente = data.get("nombre")
        contraseña_cliente=data.get("contraseña")
        try: 
            cliente=obtener_cliente_nomb_y_contra(nombre_cliente,contraseña_cliente)
        except Exception as e:
            return jsonify({"no se encontró cliente": str(e)}), 500
        
        lista_productos=[]
        productos=data.get("productos")
        try:       
            for prod in productos:

                try:
                    producto=obtener_producto_por_descripcion(prod)

                    lista_productos.append(producto.get("_id"))
                except Exception as e:
                    return jsonify({"no se encontró producto": str(e)}), 500


        except Exception as i:
            return jsonify({"error al obtener estado --": str(i)}), 500


        try:

            estado=obtener_estado_por_nombre("Carrito")
            carrito=Solicitud(lista_productos,data.get("cantidad"),cliente.get("_id"),estado.get("_id"))
            _id=insertar_solicitud(carrito)
        except Exception as e:
            return jsonify({"error al obtener estado": str(e)}), 500
        try:

            sesiones.nueva_solicitud(cliente.get("_id"),_id)
        except Exception as e:
            return jsonify({"error--": str(e)}), 500
        
        return jsonify(True),200

    except Exception as e:
        return jsonify({"error--": str(e)}), 500