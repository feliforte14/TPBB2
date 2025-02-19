from flask import Blueprint

# Importar cada Blueprint
from RUTAS.categorias.categorias_productos_GET import categorias_blue
from RUTAS.productos.productos_GET import productos_blue
from RUTAS.categorias.categorias_clientes_GET import categorias_clientes_blue

# Crear un Blueprint principal (opcional)
api_blueprint = Blueprint("api", __name__)

# Registrar los Blueprints individuales
api_blueprint.register_blueprint(categorias_blue)
api_blueprint.register_blueprint(productos_blue)
api_blueprint.register_blueprint(categorias_clientes_blue)