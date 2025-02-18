class Producto:
    def __init__(self,  descripcion, categorias,catalogo):
        self.descripcion = descripcion
        self.categorias = categorias
        self.catalogo=catalogo

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "descripcion": self.descripcion,
            "categorias": self.categorias
        }
