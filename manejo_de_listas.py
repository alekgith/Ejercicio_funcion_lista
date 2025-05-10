def agregar(lista: list, elemento) ->list :

    """Función que agrega un elemento al final de la lista.
    
    Args:
        lista(list)
    
        elemento(any): Culquier dato
     
    Returns:
        list: Muestra la lista modificada."""
    
    lista += [elemento]

    return lista


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

def eliminar(lista: list) ->any:

    """Función que elimina el último elemento de la lista y lo devuelve.
    
    Args:
        lista(list)
    
    Returns:
        any: Muestra el último elemento de la lista."""
    for i in range(len(lista)):
        lista[i]
    a = lista[i]
    del lista[i]
    return a

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

def eliminar_todos(lista: list, elemento):
    
    """Función que elimina todas las ocurrencias de un elemento de la lista.
    
    Args:
        lista(list)
    
        elemento(any): Culquier dato"""
    a=1
    while a!=0:
        a = len(lista)
        for i in range(len(lista)):
            a -=1
            if lista[i] == elemento:

                del lista[i]

                break

def vaciar_lista(lista: list):
    """Funcion que vacia la lista
    
    Args:
        lista(list)"""
    
    del lista[::]



def validar(any: str):
    """Funcion que valida si es posible transformar un str en int
    si es posible devuelve el str como int
    
    Args:
        any(str)
        
    Returns:
        int: any"""

    while type(any)!=int:
       
        if any.isdigit() == True:
            any = int(any)
            return any
        else:
            any = input("Error, introduzca un número:\n")