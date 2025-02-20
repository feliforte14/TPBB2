from flask import Blueprint, request, jsonify
from MongoDB.Services.ClienteService import *
from MongoDB.Services.CategoriaClienteService import *
usuarios = Blueprint("usuarios", __name__)  # Se usa un Blueprint en vez de crear otra app

@usuarios.route("/ususarios/nuevo", methods=["POST"])
def nuevo_usuario_POST():
    try:
        data = request.json
        nombre = data.get("nombre")
        contraseña = data.get("contraseña")
        categoria=data.get("categoria")

        cat=obtener_categoria_cliente_por_nombre(categoria)
        
        nuevo=Cliente(nombre,obtener_categoria_cliente_por_nombre(categoria).get("_id"),contraseña)
        insertar_cliente(nuevo)
        
        return jsonify({"respuesta":f"ya se registró el nuevo usuario {nombre}"}),200

    except Exception as e:
        return jsonify({"error en registrar usuario": str(e)}), 500

@usuarios.route("/usuarios/usuario",methods=["GET"])
def info__usuario():
    try:

        data =request.json
        existente=obtener_cliente_nomb_y_contra(data.get("nombre"),data.get("contraseña"))
        categoria_de_cliente=obterner_categoria_cliente_por_id_categoria(existente.get("categoria"))
        respuesta={"cliente": existente.get("nombre"), "categoría":{"nombre":categoria_de_cliente.get("nombre"),"descripcion":categoria_de_cliente.get("descripcion")},"total_compras":existente.get("total_compras"),"total_gastado":existente.get("total_gastado")}
        return jsonify( respuesta),200
                       
    except Exception as e:
        return jsonify({"error -": str(e)}), 500