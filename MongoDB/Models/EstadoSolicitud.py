class EstadoSolicitud:
    def __init__(self, id_estado, nombre_estado, descripcion):
        self.id_estado = id_estado
        self.nombre_estado = nombre_estado
        self.descripcion = descripcion

    def to_dict(self):
        """Convierte la instancia en un diccionario para MongoDB."""
        return {
            "id_estado": self.id_estado,
            "nombre_estado": self.nombre_estado,
            "descripcion": self.descripcion,
        }
