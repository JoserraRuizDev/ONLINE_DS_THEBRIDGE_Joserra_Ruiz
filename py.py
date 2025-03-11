from datetime import datetime

grupo_musical = ["ABBA", "Madonna", "Kölsch"]
generos = ["pop","electronica"]
anios = [(1972, 1982), 1983, 1995]

diccionarios_de_grupos = [{"grupo_musical": "ABBA", "genero" : "pop", "anios": (1972, 1982)}, {"grupo_musical": "Madonna", "genero" : "pop", "anios": 1983}, {"grupo_musical": "Kölsch", "genero": "electronica", "anios": 1995}]

def inserta(nombre, genero, fecha_inicio, fecha_disolucion=None):
    grupo_musical.append(nombre)
    generos.append(genero)
    if fecha_disolucion is not None:
        existencia = [fecha_inicio, fecha_disolucion]
    else:
        existencia = fecha_inicio
    anios.append(existencia)

    nuevo_grupo = {"grupo_musical": nombre, "genero": genero, "anios": existencia}
    diccionarios_de_grupos.append(nuevo_grupo)

def busca_genero(genero):
    grupos_por_genero = []
    for grupo in diccionarios_de_grupos:
        if grupo["genero"] == genero:
            grupos_por_genero.append(grupo["grupo_musical"])
    return(grupos_por_genero)

def busca_grupos(activos = True):
    grupos_por_actividad = []
    if activos == True:
        grupos_por_actividad = comprobar_tipo_fecha(int)
    else:
        grupos_por_actividad = comprobar_tipo_fecha(tuple)

    return(grupos_por_actividad)

def comprobar_tipo_fecha(type_data):
    grupos_por_actividad = []
    for grupo in diccionarios_de_grupos:
        if type(grupo["anios"]) is type_data:
             grupos_por_actividad.append(grupo["grupo_musical"])
    return grupos_por_actividad    

def busca_generos_indice(genero):
    lista_indices = []
    for grupo in diccionarios_de_grupos:
        if grupo["genero"] == genero:
            lista_indices.append(diccionarios_de_grupos.index(grupo))
    return(lista_indices)

def filtra_listas_genero(genero):
    lista_datos = busca_generos_indice(genero)
    l1, l2, l3 = [], [], []

    for grupo in diccionarios_de_grupos:
        if grupo["genero"] == genero:
            l1.append(grupo["grupo_musical"])
            l2.append(grupo["genero"])
            l3.append(grupo["anios"])
    return l1, l2, l3

def anios_activos():
    anios_activos = 0
    anio_actual = datetime.today().year
    for grupo in diccionarios_de_grupos:
        nombre = grupo["grupo_musical"]
        if type(grupo["anios"]) is int:
            anios_activos = anio_actual - grupo["anios"]
        elif type(grupo["anios"]) is tuple:
            anios_activos = grupo["anios"][1] - grupo["anios"][0]
        print(f"{nombre} --> {anios_activos} años totales.")


print("pop", busca_genero("pop"))
print("electronica", busca_genero("electronica"))

print("activos", busca_grupos())
print("disueltos", busca_grupos(False))

print("indices pop", busca_generos_indice("pop"))
print("indices electronica", busca_generos_indice("electronica"))

l1,l2,l3 = filtra_listas_genero("pop")
print("pop", l1)
print("pop", l2)
print("pop", l3)

anios_activos()