# catalogo.py
import random
from Cassandra.Config.ConeccionCasandra import AstraDBConnection
from Cassandra.Models.RegistroAlmacen import RegistroAlmacen
from MongoDB.Services.ProductoService import (
    insertar_producto, obtener_productos, eliminar_todos_los_productos
)
class Almacen:
    def __init__(self):
        self.astra_db = AstraDBConnection()
        self.collection_name = "Almacen"

    def create_collection(self):
        """Crea la colección 'Almacen' si no existe."""
        if self.collection_name not in self.astra_db.db.list_collection_names():
            self.astra_db.create_collection(self.collection_name)
            print(f"Colección '{self.collection_name}' creada.")
    def borrar_datos(self):
        if self.collection_name in self.astra_db.db.list_collection_names():
            try:
                 self.astra_db.db[self.collection_name].delete_many({})
            except Exception as e :
                print( f'no se pudo borrar los datos de la coleccion {e}')


    def insert_initial_data(self):
        self.create_collection()
        """Inserta datos iniciales en la colección 'Almacen'."""
        almacen_data = [
                ]
        existentes=obtener_productos()
        for prod in existentes:
            almacen_data.append({"_id_producto":prod.get("_id"),"stock":random.randint(1,20),"precio":random.randint(1000,2000)})
        
        self.astra_db.insert_many(self.collection_name, almacen_data)
        print(f"Datos insertados en '{self.collection_name}'.")

    def conocerPrecio(self, id_producto):
        try:
            query = {"_id_producto": id_producto}
            return self.astra_db.db[self.collection_name].find_one(query).get("precio")
        except Exception as e:
            print(f"no se encontró el precio")        
            return False
        
    def cambiarPrecio(self, id_producto, precioNuevo):
        query = {"_id_producto": id_producto}
        if precioNuevo>=1:
            update = {"$set": {"precio": precioNuevo}}  # Operación de actualización
            try:
                resultado = self.astra_db.db[self.collection_name].update_one(query, update)
                if resultado:
                    print(f"Precio del producto {id_producto} actualizado a {precioNuevo}.")
                    return True
                else:
                    print(f"No se encontró ningún producto con id {id_producto}.")
                    return False
            except Exception as e:
                print(f"Error al actualizar el precio: {e}")
                return False
        else: 
            print("no se pueden definir precios negativos ni cero")
            return False

    def conocerStock(self, id_producto):
        query = {"_id_producto": id_producto}
        documents = self.astra_db.find(self.collection_name, query)
        for doc in documents:
            return doc.get('stock')
        return None  # Si no se encuentra el producto
    
    def cambiarStock(self, id_producto, stockNuevo):
#           verificar que el stock a definir sea válido
        if stockNuevo >=0:
        
            query={"_id_producto":id_producto}
            update={"$set":{"stock":stockNuevo}}
            try:
                resultado = self.astra_db.db[self.collection_name].update_one(query, update)
                if resultado:
                    print(f"stock del producto {id_producto} actualizado a {stockNuevo}.")
                    return True
                else:
                    print(f"No se encontró ningún producto con id {id_producto}.")
                    return False
            except Exception as e:
                print(f"Error al actualizar el stock: {e}")
                return False
        else:
            print(" no se pueden definir stock menores que  cero")
            return False    

    def restarAlStockActual(self,id_producto,cantidad_a_restar):
        query={"_id_producto":id_producto}
        producto = self.astra_db.find(self.collection_name, query)
        cantidad_actual=0

        for p in producto:
            cantidad_actual=p.get("stock")

        resultado=cantidad_actual - cantidad_a_restar
        if resultado >=0:
            update={"$set":{"stock":resultado}}
            try:
                self.astra_db.db[self.collection_name].update_one(query, update)
                print(f'se actualizó el stock del producto a {resultado}')
                return True
            
            except Exception as e:

                print(f"No se encontró ningún producto con id {id_producto},{e}.")
                return False
        else:
            print(" no se pueden definir stock menores que  cero")
            return False    

    def  sumarAlStockActual(self,id_producto,cantidad_a_sumar):
        if cantidad_a_sumar>0:
            query={"_id_producto":id_producto}
            producto = self.astra_db.find_one(self.collection_name, query)
            cantidad_actual=0
            for p in producto:
                cantidad_actual=p.get("stock")
            resultado=cantidad_actual + cantidad_a_sumar
            update={"$set":{"stock":resultado}}
            try:
                self.astra_db.db[self.collection_name].update_one(query, update)
                print(f'se actualizó el stock del producto a {resultado}')
                return True
            
            except Exception as e:

                print(f"No se encontró ningún producto con id {id_producto},{e}.")
                return False
        else:
            print("no se pueden sumar negativos")
            return False
    def agregarRegistro(self,RegistroAlmacen):
        try:
            self.astra_db.db[self.collection_name].insert_one(RegistroAlmacen)
        except Exception as e:
            print(f"no se pudo agregar registro {e}")

    def find_all(self):
        documents = self.astra_db.find(self.collection_name)
        return list(documents)  # Convertir el cursor a una lista