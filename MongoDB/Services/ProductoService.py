from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.Producto import Producto

db = MongoDBConnection().db

def insertar_producto(producto: Producto):
    db.get_collection("productos").insert_one(producto.to_dict())

def obtener_productos():
    return list(db.get_collection("productos").find({}, {"_id": 0}))

def eliminar_todos_los_productos():
    """Elimina todos los documentos de la colección productos."""
    db.productos.delete_many({})
