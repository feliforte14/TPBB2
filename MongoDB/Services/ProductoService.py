from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.Producto import Producto
from MongoDB.Services.CategoriaProductoService import (
    insertar_categoria, obtener_categorias, eliminar_todas_las_categorias,obtener_categoria_por_nombre,obtener_categoria_por_id
)
db = MongoDBConnection().db

def insertar_producto(producto: Producto):
    """Inserta un producto en la base de datos"""
    try:
        db.get_collection("productos").insert_one(producto.to_dict())
        print(f"✅ Producto '{producto.descripcion}' insertado correctamente.")
        return True
    except Exception as e:
        print(f"❌ Error al insertar producto: {e}")
        return False

def obtener_productos():
    """Obtiene la lista de productos"""
    try:
        return list(db.get_collection("productos").find({}))
    except Exception as e:
        print(f"❌ Error al obtener productos: {e}")
        return []

def eliminar_todos_los_productos():
    """Elimina todos los productos de la colección y muestra la cantidad eliminada"""
    try:
        resultado = db.get_collection("productos").delete_many({})
        print(f"🗑️ {resultado.deleted_count} productos eliminados.")
        return True
    except Exception as e:
        print(f"❌ Error al eliminar productos: {e}")
        return False
    
def obtener_producto_por_id(_id_producto):
    try:
        return db.get_collection("productos").find_one({"_id":_id_producto})
    except Exception as e :
        print(f"no se pudo obtener el producto {e}")

def obtener_producto_por_descripcion(_descripcion):
    try:
        return db.get_collection("productos").find_one({"descripcion":_descripcion})
    except Exception as e :
        print(f"no se pudo obtener producto {e}")

def insertar_categoria(_id_categoria,id_producto,descripcion_categoria:None):
    try:

        db.get_collection("categorias_productos").update_one(
            {"_id":_id_categoria},
            {"$push":{"listaProductos":id_producto}}
        )

        db.get_collection("productos").update_one(
            {"_id":id_producto},
            {"$push":{"categorias":_id_categoria}}
        )
        return True
    except Exception as e:
        print(f"no se pudo agregar la categoría al producto {e}")
        return False