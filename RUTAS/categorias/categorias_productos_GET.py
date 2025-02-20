from flask import Blueprint, request, jsonify
from urllib.parse import quote, unquote
from MongoDB.Services.CategoriaProductoService import*
from MongoDB.Models.Producto import Producto
from MongoDB.Services.ProductoService import *
from Cassandra.Session import sesiones
from Cassandra.Almacen import almacen

categorias_blue = Blueprint("categorias", __name__)  # Se usa un Blueprint en vez de crear otra app

@categorias_blue.route("/categorias_productos", methods=["get"])
def categorias_productos_GET():
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
        docs=obtener_categorias ()

        for doc in docs:
            cat={"nombre":doc.get("nombre"),"descripcion":doc.get("descripcion"),"listaProductos":[]}
            prods=doc.get("listaProductos")
            for pro in prods:
                registro={"descripcion":obtener_producto_por_id(pro).get("descripcion"),"stock":almacen.conocerStock(pro),"precio":almacen.conocerPrecio(pro)}
                cat["listaProductos"].append(registro)

            respuesta.append(cat)

        return jsonify(respuesta),200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@categorias_blue.route("/categorias_productos/<nombre>", methods=["get"])
def categoria_de_productos_por_nombre_GET(nombre):
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
        docs=obtener_productos ()
    #    print(docs)

        for doc in docs:
            producto={"descripcion":doc.get("descripcion"),"categorias":[]}
            cats=doc.get("categorias")
            for cat in cats:

                producto["categorias"].append(obtener_categoria_por_id(cat).get("nombre"))
            respuesta.append(producto)

        return jsonify(respuesta),200

    except Exception as e:
        return jsonify({"error": str(e)}), 500