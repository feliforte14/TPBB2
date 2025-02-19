class Cliente:
    def __init__(self,  nombre, categoria, contraseña, total_compras=0, total_gastado=0):
        
        self.nombre = nombre
        self.categoria = categoria
        self.contraseña = contraseña  # Se recomienda encriptar
        self.total_compras = total_compras
        self.total_gastado = total_gastado

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "contraseña": self.contraseña,
            "total_compras": self.total_compras,
            "total_gastado": self.total_gastado,
        }
