class EstadoSolicitud:
    def __init__(self, nombre_estado, descripcion):
        self.nombre_estado = nombre_estado
        self.descripcion = descripcion

    def to_dict(self):
        """Convierte la instancia en un diccionario para MongoDB."""
        return {
            "nombre_estado": self.nombre_estado,
            "descripcion": self.descripcion,
        }
