from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.Solicitud import Solicitud

db = MongoDBConnection().db
solicitudes_collection = db.get_collection("solicitudes")  # 🔹 Referencia única a la colección

def insertar_solicitud(solicitud: Solicitud):
    """Inserta una solicitud en la base de datos."""
    try:
        solicitudes_collection.insert_one(solicitud.to_dict())
        print(f"✅ Solicitud con ID '{solicitud.id_solicitud}' insertada correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar solicitud: {e}")

def obtener_solicitudes():
    """Obtiene la lista de solicitudes sin el campo _id."""
    try:
        return list(solicitudes_collection.find({}, {"_id": 0}))
    except Exception as e:
        print(f"❌ Error al obtener solicitudes: {e}")
        return []

def eliminar_todas_las_solicitudes():
    """Elimina todas las solicitudes y muestra la cantidad eliminada."""
    try:
        resultado = solicitudes_collection.delete_many({})
        print(f"🗑️ {resultado.deleted_count} solicitudes eliminadas.")
    except Exception as e:
        print(f"❌ Error al eliminar solicitudes: {e}")
