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
        cliente=obtener_nomb_y_contra(nombre_cliente,contraseña_cliente)

        
        """

        data = request.json
        nombre_cliente = data.get("nombre")
        id_solicitud = data.get("id_solicitud")
        
        if not id_cliente or not id_solicitud:
            return jsonify({"error": "Faltan datos"}), 400

        resultado = procesar_datos(id_cliente, id_solicitud)
        return jsonify(resultado), 200
        """
        respuesta=[]
        productos=obtener_productos()
        
        for prods in productos:
            producto={"descripcion":prods.get("descripcion"),"categorias":[],"precio":almacen.conocerPrecio(prods.get("_id")),"stock":almacen.conocerStock(prods.get("id"))}
            cats=prods.get("categorias")
            for cat in cats:

                producto["categorias"].append(obtener_categoria_por_id(cat).get("descripcion"))
            respuesta.append(producto)

        return jsonify(respuesta),200

    except Exception as e:
        return jsonify({"error": str(e)}), 500