class Producto:
    def __init__(self,  descripcion, categorias):
        self.descripcion = descripcion
        self.categorias = categorias

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "descripcion": self.descripcion,
            "categorias": self.categorias,
        }
