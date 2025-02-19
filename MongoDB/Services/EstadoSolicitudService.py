from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.EstadoSolicitud import EstadoSolicitud
from bson import ObjectId

db = MongoDBConnection().db
estados_solicitud_collection = db.get_collection("estados_solicitud")  # 🔹 Referencia única a la colección

def insertar_estado_solicitud(estado_solicitud: EstadoSolicitud):
    """Inserta un estado de solicitud en la base de datos."""
    try:
        estados_solicitud_collection.insert_one(estado_solicitud.to_dict())
        print(f"✅ Estado de solicitud con ID '{estado_solicitud.descripcion}' insertado correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar estado de solicitud: {e}")

def obtener_estados_solicitud():
    """Obtiene la lista de estados de solicitud """
    try:
        return list(estados_solicitud_collection.find({}))
    except Exception as e:
        print(f"❌ Error al obtener estados de solicitud: {e}")
        return []

def eliminar_todos_los_estados_solicitud():
    """Elimina todos los estados de solicitud y muestra la cantidad eliminada."""
    try:
        resultado = estados_solicitud_collection.delete_many({})
        print(f"🗑️ {resultado.deleted_count} estados de solicitud eliminados.")
    except Exception as e:
        print(f"❌ Error al eliminar estados de solicitud: {e}")

def obtener_estado_por_id(id_estado):
    try:
        return estados_solicitud_collection.find_one({"_id": id_estado})

    except Exception as e:
        print(f"❌ Error al obtener estado de solicitud por ID: {e}")
        return None  
    
def obtener_estado_por_nombre(nombre_estado):
    try:
        return (estados_solicitud_collection.find_one({"nombre_estado": nombre_estado}))
    except Exception as e:
        print(f"❌ Error al obtener estados de solicitud por nombre: {e}")
        return False