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
from Cassandra.Almacen import( Almacen)
from Cassandra.Session import(Session)
Sesion=Session()
Almacen=Almacen()
Almacen.insert_initial_data()

Sesion.insert_initial_data()
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

def limpiar_y_insertar_facturas(): # Funcion para test
    factura_service = FacturaService()

    #  ¡Asegúrate de que existan solicitudes y clientes antes de crear facturas!
    #  (o usa los IDs que ya hayas insertado)

    try:
        # Creación de facturas (ejemplo).  Debes tener solicitudes aprobadas.
        id_factura1 = factura_service.crear_factura("654c2b2d2686879884662xxx", "654a8f9d4b4b4c5f886e6xxx") # RECUERDA USAR TUS PROPIOS ID
        print(f"Factura creada con ID: {id_factura1}")

        id_factura2 = factura_service.crear_factura("654c2b2d2686879884662yyy", "654a8f9d4b4b4c5f886e6yyy") # RECUERDA USAR TUS PROPIOS ID
        print(f"Factura creada con ID: {id_factura2}")

        # Obtener una factura por ID
        factura = factura_service.obtener_factura_por_id(id_factura1)
        if factura:
            print(f"\nFactura obtenida por ID: {factura}")
        
        # Obtener el id de solicitud
        id_solicitud_obtenida = factura_service.obtener_id_solicitud_de_factura(id_factura1)
        if id_solicitud_obtenida:
            print(f"\nId de solicitud obtenida por ID de factura: {id_solicitud_obtenida}")
        # Obtener facturas por cliente
        facturas_cliente = factura_service.obtener_facturas_por_cliente("654a8f9d4b4b4c5f886e6xxx")
        print(f"\nFacturas del cliente 1: {facturas_cliente}")
        
        # Obtener facturas por cliente
        facturas_cliente = factura_service.obtener_facturas_por_cliente("654a8f9d4b4b4c5f886e6yyy")
        print(f"\nFacturas del cliente 1: {facturas_cliente}")

        # Obtener todas las facturas
        todas_las_facturas = factura_service.obtener_todas_las_facturas()
        print(f"\nToda las facturas: {todas_las_facturas}")


    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"Otro error: {ex}")
    

def main():
    """ Función principal para gestionar clientes, productos y categorías en MongoDB """
    try:
        limpiar_y_insertar_clientes()
        limpiar_y_insertar_productos()
        limpiar_y_insertar_categorias()
        limpiar_y_insertar_categorias_clientes()
        limpiar_y_insertar_solicitudes()
        limpiar_y_insertar_estados_solicitud()
        limpiar_y_insertar_facturas()
        

    except Exception as e:
        print(f"❌ Error en la ejecución: {e}")

if __name__ == "__main__":
    main()
