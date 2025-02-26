from MongoDB.Config.ConeccionMongo import MongoDBConnection
from MongoDB.Models.Solicitud import Solicitud
from MongoDB.Services.EstadoSolicitudService import *
from MongoDB.Services.ProductoService import *
from MongoDB.Services.ClienteService import *
from Cassandra.Almacen import *
db = MongoDBConnection().db
solicitudes_collection = db.get_collection("solicitudes")  # 🔹 Referencia única a la colección

def insertar_solicitud(solicitud: Solicitud):
    """Inserta una solicitud en la base de datos."""
    try:
        resultado= solicitudes_collection.insert_one(solicitud.to_dict())
        
        print(f"✅ Solicitud  insertada correctamente.")
        return resultado.inserted_id
    except Exception as e:
        print(f"❌ Error al insertar solicitud: {e}")
        return False
def obtener_solicitudes():
    """Obtiene la lista de solicitudes ."""
    try:
        return list(solicitudes_collection.find({}))
    except Exception as e:
        print(f"❌ Error al obtener solicitudes: {e}")
        return []

def eliminar_todas_las_solicitudes():
    """Elimina todas las solicitudes y muestra la cantidad eliminada."""
    try:
        resultado = solicitudes_collection.delete_many({})
        print(f"🗑️ {resultado.deleted_count} solicitudes eliminadas.")
        True
    except Exception as e:
        print(f"❌ Error al eliminar solicitudes: {e}")
        False
        
def carrito_a_pedido(id_cliente,id_solicitud):
    try:
        #valida el id_de carrito
        carrito=solicitudes_collection.find_one({"_id":id_solicitud})
        productos_solicitados = carrito.get("productos")
        cantidades_solicitadas = carrito.get("cantidad")
        total_compra=0
        nuevo_estado=obtener_estado_por_nombre("Confirmado")
        for indice, producto_solicitado in enumerate(productos_solicitados):
            total_compra+= almacen.conocerPrecio(producto_solicitado) *cantidades_solicitadas[indice]
            cantidad = cantidades_solicitadas[indice]
            almacen.operarStockActual(producto_solicitado, cantidad, "resta")
        actualizar_total_compra(id_cliente,total_compra)
        solicitudes_collection.update_one({"_id":carrito.get("_id")},{"$set":{"estado_solicitud": nuevo_estado.get("_id")}})
        return True
    except Exception as e:
        print(f"no se pudo generar el pedido {e}")
        return False

