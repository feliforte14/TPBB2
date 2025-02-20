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
        encontrada=obtener_categoria_por_nombre(nombre)
       
        respuesta={
            "nombre":encontrada.get("nombre") ,
            "descipcion": encontrada.get("descripcion"),
            "listaProductos":[]
        }
    #    print(docs)
        
        for prod in encontrada.get("listaProductos"):
            p=obtener_producto_por_id(prod)
            producto={"descripcion":p.get("descripcion"),
                "stock":almacen.conocerStock(prod),
                "precio":almacen.conocerPrecio(prod)                      
                      }
            respuesta["listaProductos"].append(producto)


        return jsonify(respuesta),200

    except Exception as e:
        return jsonify({"error": str(e)}), 500