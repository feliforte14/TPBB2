class CategoriaProducto:
    def __init__(self, id_categoria, nombre, descripcion, productos_asociados=None):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos_asociados = productos_asociados or []

    def to_dict(self):
        """Convierte la instancia en un diccionario para MongoDB."""
        return {
            "id_categoria": self.id_categoria,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "productos_asociados": self.productos_asociados
        }
