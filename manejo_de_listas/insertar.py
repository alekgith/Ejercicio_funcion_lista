def insertar(lista: list, elemento, indice: int) ->list:
    """Función que inserta un elemento en un indice elegido de la lista.
    
    Args:
        lista(list)
    
        elemento(any): Culquier dato
    
        indice(int)
     
    Returns:
        list: Muestra la lista modificada."""
    
    a = lista[:indice] + [elemento] + lista[indice:]

    del lista[::]

    lista+=a

    return lista