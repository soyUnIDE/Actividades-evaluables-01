# Clonar una lista
original_lista = [1, 2, 3, 4, 5]
# Shallow copy utilizando el operador de slicing
clon_shallow = original_lista[:]
# Deep copy utilizando la función deepcopy del módulo copy
import copy
clon_deep = copy.deepcopy(original_lista)

# Imprimir las listas originales y clonadas
print("Original:", original_lista)
print("Shallow Copy:", clon_shallow)
print("Deep Copy:", clon_deep)

# Diferencia entre shallow copy y deep copy:
# Shallow copy crea una nueva lista pero mantiene referencias a los objetos internos.
# Deep copy crea una nueva lista y objetos internos totalmente independientes.

# Agregar un elemento a una lista
original_lista.append(6)

# Quitar un elemento de una lista
elemento_a_quitar = 3
original_lista.remove(elemento_a_quitar)

# Crear una lista nueva con los 4 últimos elementos de una lista
ultimos_cuatro_elementos = original_lista[-4:]

# Convertir palabras de una cadena a una lista
cadena_palabras = "Hola mundo Python"
lista_palabras = cadena_palabras.split()

# Comentarios con una línea
# Estas son operaciones comunes de listas en Python.

"""
En este bloque, hemos realizado varias operaciones con listas:
- Clonamos la lista original utilizando tanto shallow copy como deep copy.
- Agregamos un elemento y quitamos otro de la lista original.
- Creamos una nueva lista con los 4 últimos elementos.
- Convertimos una cadena de palabras a una lista.
Estos comentarios proporcionan claridad sobre el propósito y la funcionalidad de cada parte del código.
"""

# Imprimir los resultados después de las operaciones
print("Lista después de agregar y quitar elementos:", original_lista)
print("Últimos cuatro elementos:", ultimos_cuatro_elementos)
print("Lista de palabras:", lista_palabras)