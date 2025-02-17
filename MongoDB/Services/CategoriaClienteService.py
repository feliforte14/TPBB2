from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.CategoriaCliente import CategoriaCliente

db = MongoDBConnection().db
categorias_clientes_collection = db.get_collection("categorias_clientes")  # 🔹 Referencia única a la colección

def insertar_categoria_cliente(categoria_cliente: CategoriaCliente):
    """Inserta una categoría de cliente en la base de datos"""
    try:
        categorias_clientes_collection.insert_one(categoria_cliente.to_dict())
        print(f"✅ Categoría de cliente '{categoria_cliente.nombre}' insertada correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar categoría de cliente: {e}")

def obtener_categorias_clientes():
    """Obtiene la lista de categorías de clientes sin el campo _id"""
    try:
        return list(categorias_clientes_collection.find({}, {"_id": 0}))
    except Exception as e:
        print(f"❌ Error al obtener categorías de clientes: {e}")
        return []

def eliminar_todas_las_categorias_clientes():
    """Elimina todas las categorías de clientes y muestra la cantidad eliminada"""
    try:
        resultado = categorias_clientes_collection.delete_many({})
        print(f"🗑️ {resultado.deleted_count} categorías de clientes eliminadas.")
    except Exception as e:
        print(f"❌ Error al eliminar categorías de clientes: {e}")
