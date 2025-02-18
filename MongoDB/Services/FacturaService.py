from pymongo import MongoClient
from bson import ObjectId
from MongoDB.Models.Factura import Factura
from MongoDB.Services.ProductoService import obtener_producto_por_id  # Importante!

class FacturaService:
    def __init__(self, db_name="TPBB2", collection_name="Facturas"):
        self.client = MongoClient('mongodb://localhost:27017/')  # Reemplaza con tu conexión
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def crear_factura(self, id_solicitud, id_cliente):
        """Crea una nueva factura a partir de una solicitud."""
        solicitud_doc = self.collection.database.Solicitudes.find_one({"_id": ObjectId(id_solicitud)})
        if not solicitud_doc:
            raise ValueError(f"No se encontró la solicitud con ID: {id_solicitud}")

        if solicitud_doc["estado_solicitud"] != "Aprobada":  #  Verificación!
            raise ValueError(f"La solicitud {id_solicitud} no está aprobada, no se puede facturar.")

        cliente_doc = self.collection.database.Clientes.find_one({"_id": ObjectId(id_cliente)})
        if not cliente_doc:
            raise ValueError(f"No se encontró el cliente con ID: {id_cliente}")

        # Construir la lista de productos *con precios*
        productos_factura = []
        total_factura = 0
        for i, id_producto in enumerate(solicitud_doc["productos"]):
            producto = obtener_producto_por_id(id_producto)  # Usa la función del servicio de Producto!
            if not producto:
                raise ValueError(f"Producto con ID {id_producto} no encontrado.")

            cantidad = solicitud_doc["cantidad"][i]
            #  ¡OBTENER EL PRECIO! (Aquí asumo que tu Producto tiene un campo 'precio')
            #  Si el precio está en otro lugar (ej., en un catálogo), debes obtenerlo.
            precio_unitario = producto.get("precio")  #  <--  ¡CAMBIA ESTO SI ES NECESARIO!
            if precio_unitario is None:
                raise ValueError(f"El producto {id_producto} no tiene precio definido.")

            productos_factura.append({
                "id_producto": str(id_producto),
                "cantidad": cantidad,
                "precio_unitario": precio_unitario,
            })
            total_factura += cantidad * precio_unitario

        factura = Factura(
            id_solicitud=str(id_solicitud),
            id_cliente=str(id_cliente),
            total=total_factura,
            productos=productos_factura,
        )

        inserted_id = self.collection.insert_one(factura.to_dict()).inserted_id
        return str(inserted_id)

    def obtener_factura_por_id(self, id_factura):
        """Obtiene una factura por su ID."""
        factura_doc = self.collection.find_one({"_id": ObjectId(id_factura)})
        if factura_doc:
            return Factura(**factura_doc).to_dict()  # Devuelve como diccionario
        return None

    def obtener_facturas_por_cliente(self, id_cliente):
        """Obtiene todas las facturas de un cliente."""
        facturas_cursor = self.collection.find({"id_cliente": str(id_cliente)})  # Convertir a string
        facturas = [Factura(**doc).to_dict() for doc in facturas_cursor]
        return facturas

    def obtener_id_solicitud_de_factura(self, id_factura):
        """Obtiene el ID de la solicitud asociada a una factura."""
        factura_doc = self.collection.find_one({"_id": ObjectId(id_factura)})
        if factura_doc:
            return factura_doc["id_solicitud"]
        return None

    def eliminar_factura(self, id_factura):
        """Elimina una factura por su ID.  ¡Cuidado con esto en producción!"""
        result = self.collection.delete_one({"_id": ObjectId(id_factura)})
        return result.deleted_count > 0  # Devuelve True si se eliminó algo

    def actualizar_estado_factura(self, id_factura, nuevo_estado):
        """Actualiza el estado de una factura."""
        result = self.collection.update_one(
            {"_id": ObjectId(id_factura)},
            {"$set": {"estado": nuevo_estado}}
        )
        return result.modified_count > 0

    def obtener_todas_las_facturas(self):
        """
        Obtiene todas las facturas de la base de datos.
        Útil para reportes, pero puede ser lento si hay muchas facturas.
        Considera paginación para grandes conjuntos de datos.
        """
        facturas_cursor = self.collection.find()
        return [Factura(**doc).to_dict() for doc in facturas_cursor]