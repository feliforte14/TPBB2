from flask import Blueprint, request, jsonify
from urllib.parse import quote, unquote
from MongoDB.Services.CategoriaProductoService import*
from MongoDB.Models.Producto import Producto
from MongoDB.Services.ProductoService import *
from Cassandra.Almacen import almacen

productos_blue = Blueprint("productos", __name__)  # Se usa un Blueprint en vez de crear otra app

@productos_blue.route("/productos", methods=["get"])
def productos_GET():
    try:
        """
        data = request.json
        id_cliente = data.get("id_cliente")
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
    

@productos_blue.route("/productos/<descripcion>", methods=["get"])
def productos_por_descripcion_GET(descripcion):
    try:
        """
        data = request.json
        id_cliente = data.get("id_cliente")
        id_solicitud = data.get("id_solicitud")
        
        if not id_cliente or not id_solicitud:
            return jsonify({"error": "Faltan datos"}), 400

        resultado = procesar_datos(id_cliente, id_solicitud)
        return jsonify(resultado), 200
        """
        respuesta=[]
        docs=obtener_producto_por_descripcion(descripcion)
        
        for doc in docs:
            producto={"descripcion":doc.get("descripcion"),"categorias":[]}
            cats=doc.get("categorias")
            for cat in cats:

                producto["categorias"].append(obtener_categoria_por_id(cat).get("descripcion"))
            respuesta.append(producto)

        return jsonify(respuesta),200

    except Exception as e:
        return jsonify({"error": str(e)}), 500