from random import randint
from Cassandra.Models.RegistroAlmacen import RegistroAlmacen
from Cassandra.Almacen import Almacen
from MongoDB.Services.ClienteService import (
    insertar_cliente, obtener_clientes, eliminar_todos_los_clientes
)
from MongoDB.Services.ProductoService import *

from MongoDB.Services.CategoriaProductoService import (
    insertar_categoria, obtener_categorias, eliminar_todas_las_categorias,actualizar_categoria_producto
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
from MongoDB.Services.CatalogoProductoService import(
    obtener_catalogos,obtener_un_catalogo_por_id,obtener_catalogo_por_descripcion,insertar_catalogo,eliminar_todos_los_catalogos,obtener_catalogo_nombre
)
from Cassandra.Almacen import( Almacen)
from Cassandra.Session import(Session)
from MongoDB.Models.Cliente import Cliente
from MongoDB.Models.Producto import Producto
from MongoDB.Models.CatalogoProducto import CatalogoProducto
from MongoDB.Models.CategoriaProducto import CategoriaProducto
from MongoDB.Models.CatalogoProducto import CatalogoProducto
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
def limpiar_y_insertar_catalogos():
            
            try:
                eliminar_todos_los_catalogos()
                catalogos = [
                    CatalogoProducto("Lanus",[1,3]),
                    CatalogoProducto("Avellaneda",[2,4])
                    ]
                for cat in catalogos:
                    insertar_catalogo(cat)
            except Exception as e:
                print(f"no se pudo eliminar e insertar catálogos {e}")


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
    



def cargar_data_en_todos_lados():
    eliminar_todas_las_categorias()
    eliminar_todas_las_categorias_clientes()
    eliminar_todas_las_solicitudes()
    eliminar_todos_los_catalogos()
    eliminar_todos_los_clientes()
    eliminar_todos_los_estados_solicitud()
    eliminar_todos_los_productos()

    cat_prod_1=CategoriaProducto("tecnologia","cosas tecnológicas")
    cat_prod_2=CategoriaProducto("alimnetos","cosas ricas")
    
    insertar_categoria(cat_prod_1)
    insertar_categoria(cat_prod_2)
    todas_las_cat=obtener_categorias()


    prod_1=Producto("celular",[todas_las_cat[0].get("_id")])
    prod_2=Producto("coca",[todas_las_cat[1].get("_id")])
    prod_3=Producto("tablet",[todas_las_cat[0].get("_id")])
    prod_4=Producto("sanguche",[todas_las_cat[1].get("_id")])

    insertar_producto(prod_1)
    insertar_producto(prod_2)
    insertar_producto(prod_3)
    insertar_producto(prod_4)

    todos_los_prod=obtener_productos()
    actualizar_categoria_producto(todas_las_cat[0].get("_id"),todos_los_prod[0].get("_id"))
    actualizar_categoria_producto(todas_las_cat[1].get("_id"),todos_los_prod[1].get("_id"))
    actualizar_categoria_producto(todas_las_cat[0].get("_id"),todos_los_prod[2].get("_id"))
    actualizar_categoria_producto(todas_las_cat[1].get("_id"),todos_los_prod[3].get("_id"))

    catalogo1=CatalogoProducto("Lanus","productos del CATALOGO Lanus",[todos_los_prod[0].get("_id"),todos_los_prod[2].get("_id")])
    catalogo2=CatalogoProducto("Balcarce","productos del CATALOGO Balarce",[todos_los_prod[1].get("_id"),todos_los_prod[3].get("_id")])

    insertar_catalogo(catalogo1)
    insertar_catalogo(catalogo2)


    cat_cliente1=CategoriaCliente("low","clientes básicos",0.0)
    cat_cliente2=CategoriaCliente("upper","clientes premium",0.8)

    insertar_categoria_cliente(cat_cliente1)
    insertar_categoria_cliente(cat_cliente2)

    todas_las_categorias=obtener_categorias_clientes()


    cliente1=Cliente("pedro",todas_las_categorias[0].get("_id"),"contraseña1")
    cliente2=Cliente("Sabrina",todas_las_categorias[1].get("_id"),"contraseña2")
    cliente3=Cliente("Felipe",todas_las_categorias[0].get("_id"),"contraseña3")
    cliente4=Cliente("Joni",todas_las_categorias[1].get("_id"),"contraseña4",)


    insertar_cliente(cliente1)
    insertar_cliente(cliente2)
    insertar_cliente(cliente3)
    insertar_cliente(cliente4)

    todos_los_clientes=obtener_clientes()
    
    estado_solicitud1=EstadoSolicitud("Carrito","Pendiente a confirmar carrito")
    estado_solicitud2=EstadoSolicitud("Confirmado","Pendiente a facturar")
    estado_solicitud3=EstadoSolicitud("Cancelado","Carrito cancelado")
 
    insertar_estado_solicitud(estado_solicitud1)
    insertar_estado_solicitud(estado_solicitud2)
    insertar_estado_solicitud(estado_solicitud3)

    todos_los_estados_soli=obtener_estados_solicitud()

    solicitud1=Solicitud([todos_los_prod[0].get("_id"),todos_los_prod[1].get("_id")],[2,3],todos_los_clientes[0].get("_id"),todos_los_estados_soli[0].get("_Id"))
    solicitud2=Solicitud([todos_los_prod[1].get("_id"),todos_los_prod[2].get("_id")],[2,3],todos_los_clientes[1].get("_id"),todos_los_estados_soli[0].get("_Id"))
    solicitud3=Solicitud([todos_los_prod[0].get("_id"),todos_los_prod[3].get("_id")],[2,3],todos_los_clientes[0].get("_id"),todos_los_estados_soli[1].get("_Id"))

    insertar_solicitud(solicitud1)    
    insertar_solicitud(solicitud2)
    insertar_solicitud(solicitud3)

    tadas_las_solis=obtener_solicitudes()
    session=Session()
    session.create_collection()
    session.borrar_datos()

    session.iniciar_session(todos_los_clientes[0].get("_id"))

    session.nueva_solicitud(todos_los_clientes[0].get("_id"),tadas_las_solis[0]["_id"])
    session.cerrar_session(todos_los_clientes[0].get("_id"))

    session.iniciar_session(todos_los_clientes[1].get("_id"))
    session.nueva_solicitud(todos_los_clientes[1].get("_id"),tadas_las_solis[1]["_id"])
    session.cerrar_session(todos_los_clientes[1].get("_id"))

    session.iniciar_session(todos_los_clientes[0].get("_id"))
    
    session.nueva_solicitud(todos_los_clientes[0].get("_id"),tadas_las_solis[2]["_id"])
    session.cerrar_session(todos_los_clientes[0].get("_id"))
    
    almacen=Almacen()
    almacen.borrar_datos()

    reg1=RegistroAlmacen(todos_los_prod[0].get("_id"),randint(0,50),randint(0,50000))    
    reg2=RegistroAlmacen(todos_los_prod[1].get("_id"),randint(0,50),randint(0,50000))
    reg3=RegistroAlmacen(todos_los_prod[2].get("_id"),randint(0,50),randint(0,50000))
    reg4=RegistroAlmacen(todos_los_prod[3].get("_id"),randint(0,50),randint(0,50000))

    almacen.agregarRegistro(reg1)
    almacen.agregarRegistro(reg2)
    almacen.agregarRegistro(reg3)
    almacen.agregarRegistro(reg4)

def main():

    ## armar las categorías de producto
    ## armar los productos 3
    ## armar los catálogos de productos

    ## armar categoría clientes
    ## armar clientes
    
    ## armar estadosDe Solicitudes
    ## armar sesiones
    # armar solicitudes 
    # armar factura 



    """ Función principal para gestionar clientes, productos y categorías en MongoDB """
    try:

    #    cargar_data_en_todos_lados()
     #   docs=obtener_productos ()
    #    print(docs)
        """
        catalogo=obtener_catalogo_nombre("Lanus")
        cat = {
                "nombre": catalogo.get("nombre"),
                "descripcion": catalogo.get("descripcion"),
                "productos": []  # Lista para almacenar los productos del catálogo
            }
        lista=catalogo.get("listaProductos",[])
        for prod_id in lista:
                producto = obtener_producto_por_id(prod_id)  # Obtener el producto por su ID
                if producto:  # Verificar si el producto existe
                    prod_nuevo = {
                        "descripcion": producto.get("descripcion")

                    }
                    cat["productos"].append(prod_nuevo)  
        """                    

        """ 
            for doc in docs:
            cats=doc.get("categorias")
            for cat in cats:
                print(f"/n  {cat}")
        """
        """
        limpiar_y_insertar_clientes()
        
        limpiar_y_insertar_categorias()
        limpiar_y_insertar_categorias_clientes()
        limpiar_y_insertar_solicitudes()
        limpiar_y_insertar_estados_solicitud()
        limpiar_y_insertar_facturas()
        limpiar_y_insertar_productos()
        limpiar_y_insertar_catalogos()
                """
   

    except Exception as e:
            print(f"❌ Error en la ejecución: {e}")

if __name__ == "__main__":
    main()
