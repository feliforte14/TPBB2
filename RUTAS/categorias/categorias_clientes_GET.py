from flask import Blueprint, request, jsonify
from bson import ObjectId
from MongoDB.Services.CategoriaClienteService import obtener_categorias_clientes, categorias_clientes_collection

categorias_clientes_blue = Blueprint("categorias_clientes", __name__)

@categorias_clientes_blue.route("/categorias_clientes/<id_categoria>", methods=["GET"])
def obtener_descripcion_categoria_cliente(id_categoria):
    """
    Obtiene la descripción de una categoría de cliente dado su ObjectId.

    Args:
        id_categoria (str): El ObjectId de la categoría de cliente como string.

    Returns:
        JSON: Un diccionario con la descripción de la categoría si se encuentra,
              o un mensaje de error si no se encuentra o si el ID no es válido.
    """
    try:
        # 1. Validar que el id_categoria sea un ObjectId válido
        if not ObjectId.is_valid(id_categoria):
            return jsonify({"error": "ID de categoría inválido"}), 400

        # 2. Buscar la categoría por su _id (usando find_one y convirtiendo el string a ObjectId)
        categoria = categorias_clientes_collection.find_one({"_id": ObjectId(id_categoria)})

        # 3. Si no se encuentra la categoría, devolver un error 404
        if not categoria:
            return jsonify({"error": "Categoría de cliente no encontrada"}), 404

        # 4. Si se encuentra, extraer la descripción y devolverla
        descripcion = categoria.get("descripcion")
        if descripcion is None:  #Consideramos tambien si la descripción no existe
             return jsonify({"error": "La categoría no tiene descripción"}), 404

        return jsonify({"descripcion": descripcion}), 200

    except Exception as e:
        # 5. Manejar cualquier otro error (por ejemplo, de conexión a la base de datos)
        return jsonify({"error": str(e)}), 500

# --- (Opcional)  Endpoints adicionales, siguiendo el mismo patrón ---

@categorias_clientes_blue.route("/categorias_clientes", methods=["GET"])
def obtener_todas_categorias():
    """Obtiene todas las categorías de clientes."""
    try:
        categorias = obtener_categorias_clientes()
        #Convertimos el objectId a String para sacarlo del diccionario
        lista_categorias=[]
        for categoria in categorias:
            categoria_dict = {
                "id_categoria_cliente": str(categoria["_id"]),  # Convert ObjectId to string
                "nombre": categoria["nombre"],
                "descripcion": categoria["descripcion"],
            }
            #Me fijo que exista el campo descuentos
            if "descuentos" in categoria:
                categoria_dict["descuentos"] = categoria["descuentos"]
            lista_categorias.append(categoria_dict)

        return jsonify(lista_categorias), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500