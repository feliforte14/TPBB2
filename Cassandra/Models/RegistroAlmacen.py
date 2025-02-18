
class RegistroAlmacen:
    def __init__(self, _id_producto,stock,precio):
        self._id_producto=_id_producto
        self.stock=stock
        self.precio=precio

    def to_dict(self):
        return{
            "_id_producto":self._id_producto,
            "stock":self.stock,
            "precio":self.precio
        }