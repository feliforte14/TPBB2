from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.Producto import Producto

db = MongoDBConnection().db

def insertar_producto(producto: Producto):
    """Inserta un producto en la base de datos"""
    try:
        db.get_collection("productos").insert_one(producto.to_dict())
        print(f"✅ Producto '{producto.descripcion}' insertado correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar producto: {e}")

def obtener_productos():
    """Obtiene la lista de productos sin el campo _id"""
    try:
        return list(db.get_collection("productos").find({}, {"_id": 0}))
    except Exception as e:
        print(f"❌ Error al obtener productos: {e}")
        return []

def eliminar_todos_los_productos():
    """Elimina todos los productos de la colección y muestra la cantidad eliminada"""
    try:
        resultado = db.get_collection("productos").delete_many({})
        print(f"🗑️ {resultado.deleted_count} productos eliminados.")
    except Exception as e:
        print(f"❌ Error al eliminar productos: {e}")

