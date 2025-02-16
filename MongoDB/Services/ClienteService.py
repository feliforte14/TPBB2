from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.Cliente import Cliente

db = MongoDBConnection().db
clientes_collection = db.get_collection("clientes")  # 🔹 Referencia única a la colección

def insertar_cliente(cliente: Cliente):
    """Inserta un cliente en la base de datos"""
    try:
        clientes_collection.insert_one(cliente.to_dict())
        print(f"✅ Cliente '{cliente.nombre}' insertado correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar cliente: {e}")

def obtener_clientes():
    """Obtiene la lista de clientes sin el campo _id"""
    try:
        return list(clientes_collection.find({}, {"_id": 0}))
    except Exception as e:
        print(f"❌ Error al obtener clientes: {e}")
        return []

def eliminar_todos_los_clientes():
    """Elimina todos los clientes y muestra la cantidad eliminada"""
    try:
        resultado = clientes_collection.delete_many({})
        print(f"🗑️ {resultado.deleted_count} clientes eliminados.")
    except Exception as e:
        print(f"❌ Error al eliminar clientes: {e}")
