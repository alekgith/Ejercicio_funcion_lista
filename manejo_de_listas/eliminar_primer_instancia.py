def eliminar_primer_instancia(lista: list, elemento):

    """Función que elimina la primera ocurrencia de un elemento de la lista y lo devuelve.
    
    Args:
        lista(list)
    
        elemento(any): Culquier dato
     
    Returns:
        any: Muestra la primera ocurrencia de un elemento de la lista.
        None: Si no existe el elemento en la lista."""

    for i in range(len(lista)):
        a=lista[i]
        if lista[i] == elemento:
            del lista[i]
            return a
    return None
