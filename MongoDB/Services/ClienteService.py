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
    """Obtiene la lista de clientes """
    try:
        return list(clientes_collection.find({}))
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

def obtener_cliente_nomb_y_contra(nombre_cliente,contraseña_cliente):
    try:
        encontrado=clientes_collection.find_one({"nombre":nombre_cliente,"contraseña":contraseña_cliente})
       # print(f" se encontró al usuario por nombre y contraseña: {encontrado}")
        return encontrado
    except Exception as e:
        print(f"no se encontró el cliente {e}")
        return False
def actualizar_total_compra(id_cliente, total_de_compra):
    try:
        return clientes_collection.update_one({"_id":id_cliente},{"$inc":{"total_gastado": total_de_compra,"total_compras":1}})
    except Exception as e:
        print(f"no se pudo actualizar el total de compra de un cliente {e}")