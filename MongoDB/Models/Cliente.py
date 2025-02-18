class Cliente:
    def __init__(self,  nombre, tipo_cliente, contraseña, total_compras=0, total_gastado=0, categoria="LOW"):
        
        self.nombre = nombre
        self.tipo_cliente = tipo_cliente
        self.contraseña = contraseña  # Se recomienda encriptar
        self.total_compras = total_compras
        self.total_gastado = total_gastado
        self.categoria = categoria

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tipoCliente": self.tipo_cliente,
            "contraseña": self.contraseña,
            "total_compras": self.total_compras,
            "total_gastado": self.total_gastado,
            "categoria": self.categoria
        }
