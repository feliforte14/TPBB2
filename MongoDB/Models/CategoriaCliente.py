class CategoriaCliente:
    def __init__(self, id_categoria_cliente, nombre, descripcion, descuentos=None):
        self.id_categoria_cliente = id_categoria_cliente
        self.nombre = nombre
        self.descripcion = descripcion
        self.descuentos = descuentos or []  # Inicializa descuentos como lista vacía si no se pasa nada

    def to_dict(self):
        """Convierte la instancia en un diccionario para MongoDB."""
        return {
            "id_categoria_cliente": self.id_categoria_cliente,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "descuentos": self.descuentos  # Si no quieres descuentos, puedes eliminar esta línea
        }
