def obtener_indice(lista: list, elemento) ->int:
    """Función que encuentra el índice de la primera ocurrencia de un elemento en la lista.
    
    Args:
        lista(list)
    
        elemento(any): Culquier dato
     
    Returns:
        int: Muestra el indice donde se encuentra la primera ocurrencia de un elemento en la lista.
        int: Devuelve -1 si el elemento no existe en la lista."""

    for i in range(len(lista)):

        if lista[i] == elemento:
            return i
    return -1