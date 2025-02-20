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
        respuesta=[]
        productos=obtener_productos()
        
        for prods in productos:
            producto={"descripcion":prods.get("descripcion"),"categorias":[],"precio":almacen.conocerPrecio(prods.get("_id")),"stock":almacen.conocerStock(prods.get("_id"))}
            cats=prods.get("categorias")
            for cat in cats:

                producto["categorias"].append(obtener_categoria_por_id( cat).get("nombre"))
            respuesta.append(producto)

        return jsonify(respuesta),200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@productos_blue.route("/productos/<descripcion>", methods=["get"])
def productos_por_descripcion_GET(descripcion):
    try:
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