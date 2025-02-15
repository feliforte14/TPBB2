from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://jonathanmayan:PASSWORDDB1@cluster0.woepn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
cliente = MongoClient(uri, server_api=ServerApi('1'))

# Selecciona la base de datos
base_datos = cliente['base_datos_tp_ingenieria_datos2']

# Selecciona la colección
coleccion_clientes = base_datos['clientes']

# Ejecuta un comando, por ejemplo, encontrar todos los documentos en la colección 'clientes'
documentos = coleccion_clientes.find()

# Imprime los documentos
for documento in documentos:print( documento)

# Cierra la conexión
cliente.close()