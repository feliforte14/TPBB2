class CategoriaProducto:
    def __init__(self,  nombre, descripcion, listaProductos=None):
        
        self.nombre = nombre
        self.descripcion = descripcion
        self.listaProductos = listaProductos or []

    def to_dict(self):
        """Convierte la instancia en un diccionario para MongoDB."""
        return {
        
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "listaProductos": self.listaProductos
        }
