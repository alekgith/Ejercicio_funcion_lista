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