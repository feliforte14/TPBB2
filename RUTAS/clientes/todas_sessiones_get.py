from flask import Blueprint, request, jsonify
from MongoDB.Services.ClienteService import *
from Cassandra.Session import sesiones 
todas_sesion_GET = Blueprint("todas_las_sessiones", __name__)  # Se usa un Blueprint en vez de crear otra app

@todas_sesion_GET.route("/session/todas", methods=["get"])
def  todas_sesiones_de_cliente():
    data = request.json
    respuesta=[]
    try:
            nombre_cliente = data.get("nombre")
            contraseña_cliente=data.get("contraseña")
            cliente=obtener_cliente_nomb_y_contra(nombre_cliente,contraseña_cliente)
            listado=sesiones.todas_sesiones(cliente.get("_id"))
            for se in listado:
                  s=sesiones.obtener_session_por_id_sesion(se.get("_id"))
                  respuesta.append({"inicio":s.get("inicio"),"fin":s.get("fin")})
            return jsonify({"respuesta":f"{respuesta}" }),200
    except Exception as e:
          print(f"no se pudo cerrar la sesion del usuario {e}")