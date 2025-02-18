class CatalogoProducto:
    def __init__(self,descripcion,listaProductos):
        self.descripcion=descripcion
        self.listaProductos=listaProductos
    
    def to_dict(self):
        return{
            "descripcion":self.descripcion,
            "listaProductos":self.listaProductos

        }