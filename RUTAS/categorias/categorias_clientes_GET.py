from flask import Blueprint, request, jsonify
from bson import ObjectId
from MongoDB.Services.CategoriaClienteService import obtener_categorias_clientes, categorias_clientes_collection, obtener_categoria_por_nombre  # Importa la función para buscar por nombre
from MongoDB.Services.ClienteService import clientes_collection # Importa la colección de clientes

categorias_clientes_blue = Blueprint("categorias_clientes", __name__)

@categorias_clientes_blue.route("/categorias_clientes/<nombre_categoria>", methods=["GET"])
def obtener_clientes_por_categoria(nombre_categoria):
    try:
        categoria = obtener_categoria_por_nombre(nombre_categoria)

        if not categoria:
            return jsonify({"error": "Categoría de cliente no encontrada"}), 404
        
        if isinstance(categoria, list):
            categoria = categoria[0]
        
        id_categoria = str(categoria["_id"])  
        clientes_cursor = clientes_collection.find({"categoria": id_categoria})

        clientes = []
        for cliente in clientes_cursor:
            clientes.append({
                "_id": str(cliente["_id"]), 
                "nombre": cliente["nombre"]
            })

        return jsonify(clientes), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@categorias_clientes_blue.route("/categorias_clientes", methods=["GET"])
def obtener_todas_categorias():
    """Obtiene todas las categorías de clientes."""
    try:
        categorias = obtener_categorias_clientes()
        lista_categorias=[]
        for categoria in categorias:
            categoria_dict = {
                "id_categoria_cliente": str(categoria["_id"]),  # Convert ObjectId to string
                "nombre": categoria["nombre"],
                "descripcion": categoria["descripcion"],
            }
            if "descuentos" in categoria:
                categoria_dict["descuentos"] = categoria["descuentos"]
            lista_categorias.append(categoria_dict)

        return jsonify(lista_categorias), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500