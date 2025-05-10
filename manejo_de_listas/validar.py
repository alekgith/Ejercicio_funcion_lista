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