class Solicitud:
    def __init__(self, productos, cantidad, id_cliente, estado_solicitud):
        self.productos = productos  # lista de IDs de productos
        self.cantidad = cantidad    # lista de cantidades correspondientes a los productos
        self.id_cliente = id_cliente
        self.estado_solicitud = estado_solicitud

    def to_dict(self):
        """Convierte la instancia en un diccionario para MongoDB."""
        return {
            "productos": self.productos,
            "cantidad": self.cantidad,
            "id_cliente": self.id_cliente,
            "estado_solicitud": self.estado_solicitud,
        }