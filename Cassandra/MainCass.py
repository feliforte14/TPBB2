# main.py
from Almacen import Almacen
from Session import Session
sesion=Session()

catalogo=Almacen()


catalogo.insert_initial_data()
print(catalogo.find_all())

#print("Datos en 'Catalogo':")
#for doc in catalogo.find_all():    print(doc)

#el precio del producto con id 2
#print(catalogo.conocerPrecio(1))

"""
print("precio iniciar")
print(catalogo.conocerPrecio(2) )
print("modificacion:")
print(catalogo.cambiarPrecio(2,123456) )
"""
"""
print("stock inicial:")
print(catalogo.conocerStock(2))
print("modifiación stock")
print(catalogo.cambiarStock(2,0))
"""
#print(catalogo.restarAlStockActual(2,6060606060))
#conocer el stock del producto co id 3
#print(catalogo.conocerStock(100))


##sesiones

""" sesion=Session()

sesion.iniciar_session(15)

sesion.nueva_solicitud(15,"301A")
sesion.cerrar_session(15)

print(sesion.todas_sesiones(15)) """
#sesion.borrar_datos()

#sesion.insert_initial_data()

#print("---------------{555555}-------")

#print(sesion.iniciar_session(10))
#print("---------------{ln}-------")

#print(sesion.todas_sesiones(4))
#print("---------------{ln}-------")

#print(sesion.cerrar_session(10))
#print("---------------{ln}-------")



#print(sesion.iniciar_session(10))
#print("---------------{ln}-------")
#print(sesion.cerrar_session(10))
#print("---------------{ln}-------")
#print(sesion.todas_sesiones(10))
"""
print("---------------{ln}-------")
print(sesion.todas_sesiones(4))
print("---------------{ln}-------")
print(sesion.ultima_solicitud(4) )
"""