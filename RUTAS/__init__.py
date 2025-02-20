from flask import Blueprint

# Importar cada Blueprint
from RUTAS.categorias.categorias_productos_GET import categorias_blue
from RUTAS.productos.productos_GET import productos_blue
#from RUTAS.categorias.categorias_clientes_GET import categorias_clientes_blue
from RUTAS.catalogos.catalogos_GET import catalogos_blue
from RUTAS.productos.guardar_carrito_POST import carrito_post_blue
from RUTAS.productos.hacer_pedido_POST import hacer_pedido_post_blue
from RUTAS.clientes.iniciar_sesion_POST import iniciar_sesion_POST
from RUTAS.clientes.registrar_usuario_POST import usuarios

# Crear un Blueprint principal (opcional)
api_blueprint = Blueprint("api", __name__)

# Registrar los Blueprints individuales
api_blueprint.register_blueprint(categorias_blue)
api_blueprint.register_blueprint(productos_blue)
#api_blueprint.register_blueprint(categorias_clientes_blue)
api_blueprint.register_blueprint(catalogos_blue)
api_blueprint.register_blueprint(carrito_post_blue)
api_blueprint.register_blueprint(hacer_pedido_post_blue)
api_blueprint.register_blueprint(iniciar_sesion_POST)
api_blueprint.register_blueprint(usuarios)