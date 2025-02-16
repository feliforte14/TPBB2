# main.py
from cassandraConeccion import AstraDBConnection

# Inicializar la conexión
astra_db = AstraDBConnection()

# Verificar si las colecciones ya existen
catalogo_exists = "Catalogo" in astra_db.db.list_collection_names()
session_exists = "Session" in astra_db.db.list_collection_names()

# Crear colecciones solo si no existen
if not catalogo_exists:
    astra_db.create_collection("Catalogo")
    print("Colección 'Catalogo' creada.")

if not session_exists:
    astra_db.create_collection("Session")
    print("Colección 'Session' creada.")

# Insertar datos en `Catalogo` solo si la colección estaba vacía
if not catalogo_exists:
    catalogo_data = [
        {"id_catalogo": 1, "producto": 1, "stock": 100, "precio": 50},
        {"id_catalogo": 2, "producto": 2, "stock": 150, "precio": 75},
        {"id_catalogo": 3, "producto": 3, "stock": 200, "precio": 100},
        {"id_catalogo": 4, "producto": 4, "stock": 250, "precio": 125},
        {"id_catalogo": 5, "producto": 5, "stock": 300, "precio": 150},
    ]
    astra_db.insert_many("Catalogo", catalogo_data)
    print("Datos insertados en 'Catalogo'.")

# Insertar datos en `Session` solo si la colección estaba vacía
if not session_exists:
    session_data = [
        {"id_sesion": 1, "id_cliente": 1, "inicio": "2025-01-01T00:00:00", "fin": "2025-01-02T00:00:00", "id_solicitud": 1},
        {"id_sesion": 2, "id_cliente": 2, "inicio": "2025-01-03T00:00:00", "fin": "2025-01-04T00:00:00", "id_solicitud": 2},
        {"id_sesion": 3, "id_cliente": 3, "inicio": "2025-01-05T00:00:00", "fin": "2025-01-06T00:00:00", "id_solicitud": 3},
        {"id_sesion": 4, "id_cliente": 4, "inicio": "2025-01-07T00:00:00", "fin": "2025-01-08T00:00:00", "id_solicitud": 4},
        {"id_sesion": 5, "id_cliente": 5, "inicio": "2025-01-09T00:00:00", "fin": "2025-01-10T00:00:00", "id_solicitud": 5},
    ]
    astra_db.insert_many("Session", session_data)
    print("Datos insertados en 'Session'.")

# Verificar los datos insertados
print("Datos en 'Catalogo':")
documents = astra_db.find("Catalogo")
for doc in documents:
    print(doc)

# Cerrar la conexión (si es necesario)
# astra_db.client.close()  # No es necesario en este caso, pero se puede agregar si el cliente lo requiere.