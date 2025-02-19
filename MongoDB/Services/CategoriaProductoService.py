from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.CategoriaProducto import CategoriaProducto

db = MongoDBConnection().db
categorias_collection = db.get_collection("categorias_productos")  # 🔹 Referencia única a la colección

def insertar_categoria(categoria: CategoriaProducto):
    """Inserta una categoría de producto en la base de datos"""
    try:
        categorias_collection.insert_one(categoria.to_dict())
        print(f"✅ Categoría '{categoria.nombre}' insertada correctamente.")
        return True
    except Exception as e:
        print(f"❌ Error al insertar categoría: {e}")
        return False
    
def obtener_categorias():
    """Obtiene la lista de categorías """
    try:
        return list(categorias_collection.find({}))
    except Exception as e:
        print(f"❌ Error al obtener categorías: {e}")
        return []

def eliminar_todas_las_categorias():
    """Elimina todas las categorías de productos y muestra la cantidad eliminada"""
    try:
        resultado = categorias_collection.delete_many({})
        print(f"🗑️ {resultado.deleted_count} categorías eliminadas.")
        return True
    except Exception as e:
        print(f"❌ Error al eliminar categorías: {e}")
        return False
    
def obtener_categoria_por_id(_id_categoria):
    try:
        return categorias_collection.find_one({"_id":_id_categoria})
    except Exception as e:
        print(f"no se encontró la categoría buscada {e}")
        return False
    
def obtener_categoria_por_descripcion(_descripcion):
    try:
        return categorias_collection.find({"descripcion":_descripcion})
    except Exception as e:
        print(f"no se encontró la categoría buscada  {e}")
        return False
