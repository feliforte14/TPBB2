from MongoDB.Services.ClienteService import (
    insertar_cliente, obtener_clientes, eliminar_todos_los_clientes
)
from MongoDB.Services.ProductoService import (
    insertar_producto, obtener_productos, eliminar_todos_los_productos
)
from MongoDB.Services.CategoriaProductoService import (
    insertar_categoria, obtener_categorias, eliminar_todas_las_categorias
)
from MongoDB.Services.CategoriaClienteService import (
    insertar_categoria_cliente, obtener_categorias_clientes, eliminar_todas_las_categorias_clientes
)
from MongoDB.Services.SolicitudService import (
    insertar_solicitud, obtener_solicitudes, eliminar_todas_las_solicitudes
)
from MongoDB.Services.EstadoSolicitudService import (
    insertar_estado_solicitud, obtener_estados_solicitud, eliminar_todos_los_estados_solicitud
)



from MongoDB.Models.Cliente import Cliente
from MongoDB.Models.Producto import Producto
from MongoDB.Models.CategoriaProducto import CategoriaProducto
from MongoDB.Models.CategoriaCliente import CategoriaCliente
from MongoDB.Models.Solicitud import Solicitud
from MongoDB.Models.EstadoSolicitud import EstadoSolicitud

def limpiar_y_insertar_clientes():
    """Elimina todos los clientes y los reinserta en la base de datos."""
    print("\n🧹 Eliminando todos los clientes...")
    eliminar_todos_los_clientes()

    clientes = [
        Cliente(1, "Josefa", 2, 11),
        Cliente(2, "Enrique", 1, 12),
        Cliente(3, "Samanta", 1, 13)
    ]
    
    for cliente in clientes:
        insertar_cliente(cliente)

    print("\n✅ Clientes insertados:")
    for cliente in obtener_clientes():
        print(cliente)

def limpiar_y_insertar_productos():
    """Elimina todos los productos y los reinserta en la base de datos."""
    print("\n🧹 Eliminando todos los productos...")
    eliminar_todos_los_productos()

    productos = [
        Producto(1, "VASO", [1, 4]),
        Producto(2, "PELOTA", [2]),
        Producto(3, "SOGA", [2, 4]),
        Producto(4, "REPOSERA", [3, 4])
    ]
    
    for producto in productos:
        insertar_producto(producto)

    print("\n✅ Productos insertados:")
    for producto in obtener_productos():
        print(producto)

def limpiar_y_insertar_categorias():
    """Elimina todas las categorías de productos y las reinserta."""
    print("\n🧹 Eliminando todas las categorías de productos...")
    eliminar_todas_las_categorias()

    categorias = [
        CategoriaProducto(1, "Electrónica", "Gadgets y dispositivos", [2, 5]),
        CategoriaProducto(2, "Deportes", "Equipamiento deportivo", [3, 6]),
        CategoriaProducto(3, "Hogar", "Artículos para el hogar", [1, 4])
    ]
    
    for categoria in categorias:
        insertar_categoria(categoria)

    print("\n✅ Categorías insertadas:")
    for categoria in obtener_categorias():
        print(categoria)


def limpiar_y_insertar_categorias_clientes():
    """Elimina todas las categorías de clientes y las reinserta."""
    print("\n🧹 Eliminando todas las categorías de clientes...")
    eliminar_todas_las_categorias_clientes()

    categorias_clientes = [
        CategoriaCliente(1, "Básico", "Clientes con compras limitadas"),
        CategoriaCliente(2, "Premium", "Clientes con compras frecuentes"),
        CategoriaCliente(3, "VIP", "Clientes con compras exclusivas")
    ]
    
    for categoria_cliente in categorias_clientes:
        insertar_categoria_cliente(categoria_cliente)

    print("\n✅ Categorías de clientes insertadas:")
    for categoria_cliente in obtener_categorias_clientes():
        print(categoria_cliente)


def limpiar_y_insertar_solicitudes():
    """Elimina todas las solicitudes y las reinserta en la base de datos."""
    print("\n🧹 Eliminando todas las solicitudes...")
    eliminar_todas_las_solicitudes()

    solicitudes = [
        Solicitud(1, [1, 3], [2, 1], 1, "Pendiente"),
        Solicitud(2, [2, 4], [1, 2], 2, "Aprobada"),
        Solicitud(3, [1, 4], [3, 1], 3, "Cancelada")
    ]
    
    for solicitud in solicitudes:
        insertar_solicitud(solicitud)

    print("\n✅ Solicitudes insertadas:")
    for solicitud in obtener_solicitudes():
        print(solicitud)

def limpiar_y_insertar_estados_solicitud():
    """Elimina todos los estados de solicitud y los reinserta en la base de datos."""
    print("\n🧹 Eliminando todos los estados de solicitud...")
    eliminar_todos_los_estados_solicitud()

    estados = [
        EstadoSolicitud(1, "Pendiente", "La solicitud está pendiente de revisión."),
        EstadoSolicitud(2, "Aprobada", "La solicitud ha sido aprobada."),
        EstadoSolicitud(3, "Cancelada", "La solicitud ha sido cancelada."),
        EstadoSolicitud(4, "En Proceso", "La solicitud está siendo procesada."),
        EstadoSolicitud(5, "Completada", "La solicitud ha sido completada.")
    ]
    
    for estado in estados:
        insertar_estado_solicitud(estado)

    print("\n✅ Estados de solicitud insertados:")
    for estado in obtener_estados_solicitud():
        print(estado)

def main():
    """ Función principal para gestionar clientes, productos y categorías en MongoDB """
    try:
        limpiar_y_insertar_clientes()
        limpiar_y_insertar_productos()
        limpiar_y_insertar_categorias()
        limpiar_y_insertar_categorias_clientes()
        limpiar_y_insertar_solicitudes()
        limpiar_y_insertar_estados_solicitud()

    except Exception as e:
        print(f"❌ Error en la ejecución: {e}")

if __name__ == "__main__":
    main()
