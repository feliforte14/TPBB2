class Solicitud:
    def __init__(self, id_solicitud, productos, cantidad, id_cliente, estado_solicitud):
        self.id_solicitud = id_solicitud
        self.productos = productos  # lista de IDs de productos
        self.cantidad = cantidad    # lista de cantidades correspondientes a los productos
        self.id_cliente = id_cliente
        self.estado_solicitud = estado_solicitud

    def to_dict(self):
        """Convierte la instancia en un diccionario para MongoDB."""
        return {
            "id_solicitud": self.id_solicitud,
            "productos": self.productos,
            "cantidad": self.cantidad,
            "id_cliente": self.id_cliente,
            "estado_solicitud": self.estado_solicitud,
        }