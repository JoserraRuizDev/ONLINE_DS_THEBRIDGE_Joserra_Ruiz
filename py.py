import numpy as np

cantidades_rafa = np.array([6,5,3,1])
cantidades_nacho = np.array([3,6,2,2])
cantidades_clara = np.array([3,4,3,1])

precios_starbucks = np.array([1,2.5,4.5,17])
precios_manolo_bakes = np.array([1.5,2,5,16])

lista_precios = np.array([precios_starbucks, precios_manolo_bakes])

def precios_calculados(cliente):
    return cliente.dot(lista_precios)

precios_rafa = precios_calculados(cantidades_rafa)
precios_nacho = precios_calculados(cantidades_nacho)
precios_clara = precios_calculados(cantidades_clara)

print("Rafa:",precios_rafa)
print("Nacho:",precios_nacho)
print("Clara:",precios_clara)

def comparativa_precios(cliente):
    precios = np.sum(cliente, axis=1)
    if precios[0] < precios[1]:
        return f"debería comprar en Starbucks por {precios[0]}€."
    elif precios[1] < precios[0]:
        return f"debería comprar en Manolo Bakes por {precios[1]}€"
    else:
        return f"da igual donde compre, costará {precios[0]}€."

print(f"Rafa {comparativa_precios(precios_rafa)}")
print(f"Nacho {comparativa_precios(precios_nacho)}")
print(f"Clara {comparativa_precios(precios_clara)}")
