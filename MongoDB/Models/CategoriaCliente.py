class CategoriaCliente:
    def __init__(self,  nombre, descripcion, descuentos=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.descuentos = descuentos or []  # Inicializa descuentos como lista vacía si no se pasa nada

    def to_dict(self):
        """Convierte la instancia en un diccionario para MongoDB."""
        return {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "descuentos": self.descuentos  # Si no quieres descuentos, puedes eliminar esta línea
        }
