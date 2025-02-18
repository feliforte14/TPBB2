from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.CatalogoProducto import CatalogoProducto

db=MongoDBConnection().db
catalogos_collection=db.get_collection("catalogos_producto")

def insertar_catalogo(catalogo:CatalogoProducto):
    
    try:
        catalogos_collection.insert_one(catalogo.to_dict())
        print(f"✅ Catalogo '{catalogo.nombre}' insertado correctamente.")
    except Exception as e:
        print(f" Error al insertar catalogo: {e}")

def obtener_catalogos():

    try:
        return list(catalogos_collection.find({}))
    except Exception as e:
        print(f"Error al obtener listado de catálogos: {e}")

def obtener_un_catalogo(_id_catalogo):
    try:
        
        return catalogos_collection.find_one({"_id":_id_catalogo})
    except Exception as e:
        print(f"Error al obtener el listado de productos de un catálogo {e}")
def eliminar_todos_los_catalogos():
    try:
        resultado= catalogos_collection.delete_many({})
        print(f"🗑️ {resultado.deleted_count} catálogos de productos eliminados.")
    except Exception as e:
        print(f"Error al eliminar los catálogos de productos {e}")
