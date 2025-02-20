from flask import Blueprint, request, jsonify
from MongoDB.Services.CatalogoProductoService import *
from MongoDB.Models.CatalogoProducto import *
from MongoDB.Models.Producto import *
from MongoDB.Services.ProductoService import *
from Cassandra.Almacen import almacen
catalogos_blue = Blueprint("categologo", __name__)

@catalogos_blue.route("/catalogos", methods=["GET"])

def obtener_catalogos__():
    
    try:
        respuesta = []
        catalogos = obtener_catalogos()

        for catalogo in catalogos:
            cat = {
                "nombre": catalogo.get("nombre"),
                "descripcion": catalogo.get("descripcion"),
                "productos": []  # Lista para almacenar los productos del catálogo
            }
            
            lista_productos = catalogo.get("listaProductos", [])
            
            for prod_id in lista_productos:
                producto = obtener_producto_por_id(prod_id)  # Obtener el producto por su ID
                if producto:  # Verificar si el producto existe
                    prod_nuevo = {
                        "descripcion": producto.get("descripcion"),
                        "stock":almacen.conocerStock(prod_id),
                        "precio":almacen.conocerPrecio(prod_id)

                    }
                    cat["productos"].append(prod_nuevo)  
            
            respuesta.append(cat)    
        return jsonify(respuesta), 200
    except Exception as e:
        print(f"error en catalogos {e}")
        return jsonify(f"error en obtener catálogos  {e}"), 404


@catalogos_blue.route("/catalogos/<nombre>", methods=["GET"])
def obtener_catalogo_nombre_(nombre):
    respuesta=[]
    try:
        catalogo=obtener_catalogo_nombre(nombre)
        cat = {
                "nombre": catalogo.get("nombre"),
                "descripcion": catalogo.get("descripcion"),
                "productos": []  # Lista para almacenar los productos del catálogo
            }
        lista=catalogo.get("listaProductos",[])
        for prod_id in lista:
                producto = obtener_producto_por_id(prod_id)  # Obtener el producto por su ID
                if producto:  # Verificar si el producto existe
                    prod_nuevo = {
                        "descripcion": producto.get("descripcion"),
                        "stock":almacen.conocerStock(prod_id),
                        "precio":almacen.conocerPrecio(prod_id)
                    }
                    cat["productos"].append(prod_nuevo)  
                    
        respuesta.append(cat)
        return jsonify(respuesta), 200

    except Exception as e:
        return jsonify(f"error en obtener catálogo{nombre}  {e}"), 404