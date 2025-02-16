from MongoDB.Services.ClienteService import (
    insertar_cliente, obtener_clientes, eliminar_todos_los_clientes
)
from MongoDB.Services.ProductoService import (
    insertar_producto, obtener_productos, eliminar_todos_los_productos
)
from MongoDB.Models.Cliente import Cliente
from MongoDB.Models.Producto import Producto

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

def main():
    """ Función principal para gestionar clientes y productos en MongoDB """
    try:
        limpiar_y_insertar_clientes()
        limpiar_y_insertar_productos()
    except Exception as e:
        print(f"❌ Error en la ejecución: {e}")

if __name__ == "__main__":
    main()
