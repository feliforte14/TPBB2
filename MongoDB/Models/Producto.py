class Producto:
    def __init__(self, id_producto, descripcion, categorias):
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.categorias = categorias

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "descripcion": self.descripcion,
            "categorias": self.categorias
        }
