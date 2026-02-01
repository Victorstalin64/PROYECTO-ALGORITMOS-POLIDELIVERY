def busqueda_lineal(lista, nombre):
    
    #Búsqueda lineal de un centro por nombre
    #Retorna el diccionario del centro si lo encuentra, de lo contrario None
    
    for elemento in lista:
        if elemento["nombre"].lower() == nombre.lower():
            return elemento
    return None
