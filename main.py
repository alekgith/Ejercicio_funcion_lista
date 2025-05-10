import manejo_de_listas.agregar as lista_agregar
import manejo_de_listas.insertar as lista_insertar
import manejo_de_listas.obtener_indice as lista_indice
import manejo_de_listas.eliminar as lista_eliminar_1
import manejo_de_listas.eliminar_primer_instancia as lista_eliminar_2
import manejo_de_listas.eliminar_todos as lista_eliminar_3
import manejo_de_listas.vaciar_lista as lista_vaciar
import manejo_de_listas.validar as validacion
            
a = input("Introduzca el tamaño de la lista:\n")

a = validacion.validar(a)

lista = [None]*a

for i in range(len(lista)):
    b = input("Escriba un elemento de la lista:\n")

    lista[i]=b

print(f"Lista: {lista}")

c = input("Agrega un elemento al final: \n")

lista_agregar.agregar(lista,c)

print(lista)

d = input("Inserta un elemento: \n")

indice = input("Elija la posición en la que quiera agregar el elemento\n")

indice = validacion.validar(indice)

lista_insertar.insertar(lista,d,indice)

print(lista)

element = input("Escriba un elemento para obtener su primera posición\n")

f = lista_indice.obtener_indice(lista,element)

if f > -1:
    print(f"La primer posición de {element} se encuentra en {f}\n")
else:
    print(f"{f}/ no se encuentra el elemento\n")

print("Eliminando el último elemento de la lista")

lista_eliminar_1.eliminar(lista)

print(f"{lista}\n")

element= input("Escriba un elemento para borrar su primer ocurrencia\n")

print("Eliminando la primer ocurrencia de un elemento de la lista")

lista_eliminar_2.eliminar_primer_instancia(lista,element)

print(lista)

element = input("Escriba un elemento para borrar todas sus ocurrencias\n")

print(f"Eliminando todas las ocurrencias de {element}")

lista_eliminar_3.eliminar_todos(lista, element)

print(lista)

lista_vaciar.vaciar_lista(lista)

print("Vaciando la lista")

print(lista)