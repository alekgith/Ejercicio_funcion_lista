from manejo_de_listas import*
            
a = input("Introduzca el tamaño de la lista:\n")

a = validar(a)

lista = [None]*a

for i in range(len(lista)):
    b = input("Escriba un elemento de la lista:\n")

    lista[i]=b

print(f"Lista: {lista}")

c = input("Agrega un elemento al final: \n")

agregar(lista,c)

print(lista)

d = input("Inserta un elemento: \n")

indice = input("Elija la posición en la que quiera agregar el elemento\n")

indice = validar(indice)

insertar(lista,d,indice)

print(lista)

element = input("Escriba un elemento para obtener su primera posición\n")

f = obtener_indice(lista,element)

if f > -1:
    print(f"La primer posición de {element} se encuentra en {f}\n")
else:
    print(f"{f}/ no se encuentra el elemento\n")

print("Eliminando el último elemento de la lista")

eliminar(lista)

print(f"{lista}\n")

element= input("Escriba un elemento para borrar su primer ocurrencia\n")

print("Eliminando la primer ocurrencia de un elemento de la lista")

eliminar_primer_instancia(lista,element)

print(lista)

element = input("Escriba un elemento para borrar todas sus ocurrencias\n")

print(f"Eliminando todas las ocurrencias de {element}")

eliminar_todos(lista, element)

print(lista)

vaciar_lista(lista)

print("Vaciando la lista")

print(lista)