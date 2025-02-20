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

def obtener_un_catalogo_por_id(_id_catalogo, descripcion=None):
    try:
        query = {"_id": _id_catalogo}
        if descripcion:
            query["descripcion"] = descripcion
        
        return catalogos_collection.find_one(query)
    except Exception as e:
        print(f"Error al obtener el listado de productos de un catálogo: {e}")

def obtener_catalogo_por_descripcion(descripcion, _id_catalogo=None):
    try:
        # Construir la consulta con la descripción obligatoria
        query = {"descripcion": descripcion}
        
        # Si se proporciona un _id, agregarlo a la consulta
        if _id_catalogo:
            query["_id"] = _id_catalogo
        
        # Realizar la búsqueda en la colección
        return catalogos_collection.find_one(query)
    except Exception as e:
        print(f"Error al obtener el catálogo: {e}")
        return False
def obtener_catalogo_nombre(nombre):
    try:
        # Realizar la búsqueda en la colección
        return catalogos_collection.find_one({"nombre":nombre})
    except Exception as e:
        print(f"Error al obtener el catálogo: {e}")
        return False
def eliminar_todos_los_catalogos():
    try:
        resultado= catalogos_collection.delete_many({})
        print(f"🗑️ {resultado.deleted_count} catálogos de productos eliminados.")
        return True
    except Exception as e:
        print(f"Error al eliminar los catálogos de productos {e}")
    return False

def insertar_producto_en_catalogo(descripcion_catalogo,_id_producto):
    try:
        try:
            encontrado=obtener_catalogo_por_descripcion(descripcion_catalogo)
            
            catalogos_collection.update_one(
                {"_id": encontrado.get("_id")},  # Filtro para encontrar el catálogo
                {"$push": {"listaProductos": _id_producto}}  # Operación para agregar el producto
            )
            return True
        except Exception as e:
            print(f"no se encontró el catálogo {e}")
    except Exception as e:
        print(f"no se pudo insertar el producto en el catálogo {e}")
    return False
