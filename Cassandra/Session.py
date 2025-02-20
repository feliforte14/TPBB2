# session.py
from astrapy import constants

from Cassandra.Config.ConeccionCasandra import AstraDBConnection 
from datetime import datetime

class Session:
    def __init__(self):
        self.astra_db = AstraDBConnection()
        self.collection_name = "Session"

    def create_collection(self):
        """Crea la colección 'Session' si no existe."""
        if self.collection_name not in self.astra_db.db.list_collection_names():
            self.astra_db.create_collection(self.collection_name)
            print(f"Colección '{self.collection_name}' creada.")


    def borrar_datos(self):
        if self.collection_name in self.astra_db.db.list_collection_names():
            try:
                 self.astra_db.db[self.collection_name].delete_many({})
                 return True
            except Exception as e :
                print( f'no se pudo borrar los datos de la coleccion {e}')
                return False
    def iniciar_session(self, id_cliente):
        try:

            # Crear la nueva sesión
            inicio = datetime.now().isoformat() 
            nueva_sesion = {
                "id_cliente": id_cliente,
                "inicio": inicio,
                "fin": None,  # La sesión no tiene fin al iniciarse
                "id_solicitud": None  # La sesión no tiene solicitud al iniciarse
            }

            # Insertar la nueva sesión
            self.astra_db.insert_many(self.collection_name, [nueva_sesion])
            print(f"Sesión iniciada para el cliente {id_cliente}.")
            return True
        except Exception as e:
            print(f"No se pudo iniciar la sesión: {e}")
            return False
        
    def cerrar_session(self, id_cliente):
        
        try:
            # Obtener la fecha y hora actual en formato ISO
            result=False
            fin = datetime.now().isoformat()
            try:
                result = self.astra_db.db[self.collection_name].find_one(
            
                                {"id_cliente": id_cliente},
                        sort={
                            "inicio": constants.SortDocuments.ASCENDING,
                        },
                        projection={"_id": True}
                )
            except Exception as o:
                print( f"error en la búsqueda de la última session {o}")
            if result:
                # Obtener el id_sesion de la última sesión
                
                id_sesion = result.get("_id")

                # Actualizar el campo 'fin' de la última sesión
              
                self.astra_db.db[self.collection_name].update_one(           
                            {"_id":id_sesion},
                            {"$set":{"fin": fin}} 
                )

                print(f"Sesión {id_sesion} del cliente {id_cliente} cerrada correctamente.")
                return True
            else:
                print(f"No se encontraron sesiones abiertas para el cliente {id_cliente}.")
                return False
        except Exception as e:
            print(f"No se pudo cerrar la sesión: {e}")
            return False

    def nueva_solicitud(self, id_cliente, id_solicitud):
        try:
            result=False
            try:
                result = self.astra_db.db[self.collection_name].find_one(
                
                        
                            {"id_cliente": id_cliente},
                                
                        
                            sort={
                                "inicio": constants.SortDocuments.ASCENDING,
                            },
                            projection={"_id":1}
                    )
                print(f"resultado de búsqueda: {result}")            

                self.astra_db.db[self.collection_name].update_one(           
                                        {"_id": result["_id"]},
                                        {"$set":{"id_solicitud": id_solicitud}} 
                            )    
                return True
            except Exception as e:

                                
                    print(f"No se encontraron sesiones para el cliente {id_cliente}.")
                    return False
        except Exception as e:
            print(f"No se pudo asignar la solicitud a la sesión: {e}")
            return False
    
    def ultima_solicitud(self,id_cliente):
        result=False
        try:
            result = self.astra_db.db[self.collection_name].find_one(        
            { "id_cliente": id_cliente},
            sort={ "inicio": constants.SortDocuments.ASCENDING,},projection={"_id": True}
            )
            print(f"la ultima solicitud del usuario {id_cliente}   es: {result.get("id_solicitud")}")
            return result.get("id_solicitud")
        except Exception as e:
            print( f"no se encontró una solicitud en la última sesion del cliente")
            return False
        
    def todas_sesiones(self,id_cliente):
        filtro={"id_cliente":id_cliente}
        try:
            sesiones_existentes=self.astra_db.find(self.collection_name,filtro)
            return list(sesiones_existentes)
        except Exception as e:
            print(f'no se encontraron sesiones  {e}')
            return False
        
    def obtener_session_por_id_sesion(self,_id_session):
        try:
            return self.astra_db.db[self.collection_name].find_one({"_id":_id_session})
        except Exception as e:
            print(f"no se encontró la session buscada {e}")
            return False

    def find_all(self):
        documents = self.astra_db.find(self.collection_name)
        for doc in documents:
            print(doc)

        return list(documents)
sesiones=Session()