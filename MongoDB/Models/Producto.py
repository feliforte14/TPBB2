class Producto:
    def __init__(self,  descripcion, categorias):
        self.descripcion = descripcion
        self.categorias = categorias

    def to_dict(self):
        return {
            "descripcion": self.descripcion,
            "categorias": self.categorias,
        }
