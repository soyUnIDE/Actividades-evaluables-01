# Lista de listas con tamaño y peso
datos = [
    [180, 75],
    [160, 65],
    [175, 70],
    [180, 70],
    [160, 60]
]

# Definición de la key function
def key_function(item):
    """
    Key function que devuelve una tupla con el negativo del tamaño
    (para ordenar de mayor a menor altura) y el peso (para ordenar
    de menor a mayor peso en caso de igualdad en el tamaño).

    La "key function" proporciona un criterio personalizado para la
    ordenación de los elementos en la lista. En este caso, el negativo
    del tamaño se utiliza para ordenar de mayor a menor altura, y el
    peso se utiliza para romper la igualdad en el tamaño ordenando de
    menor a mayor peso. Es una manera flexible y poderosa de personalizar
    la lógica de ordenación según los requisitos específicos del programa.
    """
    return (-item[0], item[1])

# Ordenar la lista utilizando la key function
datos_ordenados = sorted(datos, key=key_function)

# Imprimir la lista original y la lista ordenada
print("Lista Original:", datos)
print("Lista Ordenada:", datos_ordenados)
