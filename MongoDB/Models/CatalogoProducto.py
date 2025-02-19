class CatalogoProducto:
    def __init__(self,nombre,descripcion,listaProductos):
        self.nombre=nombre
        self.descripcion=descripcion
        self.listaProductos=listaProductos
    
    def to_dict(self):
        return{
            "nombre":self.nombre,
            "descripcion":self.descripcion,
            "listaProductos":self.listaProductos

        }