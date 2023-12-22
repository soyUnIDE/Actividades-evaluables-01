# Función que recibe dos números y devuelve la suma
def suma_numeros(a, b):
    """
    Esta función toma dos números como entrada y devuelve su suma.
    """
    resultado = a + b
    return resultado

# Función que recibe una lista y modifica los valores doblando cada elemento (paso por referencia)
def doblar_valores_en_sitio(lista):
    """
    Esta función toma una lista como entrada y modifica la misma lista,
    doblando los valores de todos los elementos.
    """
    for i in range(len(lista)):
        lista[i] *= 2

# Función que recibe una lista y devuelve una copia de la lista original con valores doblados (paso por valor)
def doblar_valores_con_copia(lista):
    """
    Esta función toma una lista como entrada, crea una copia de la lista original
    y devuelve la copia con los valores doblados. La lista original no se modifica.
    """
    lista_copia = lista.copy()  # Se crea una copia de la lista original
    for i in range(len(lista_copia)):
        lista_copia[i] *= 2
    return lista_copia

# Ejemplo de uso de las funciones
num1 = 5
num2 = 7
resultado_suma = suma_numeros(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado_suma}")

# Lista original
mi_lista = [1, 2, 3, 4, 5]
print("Lista original:", mi_lista)

# Modificar la lista original en su lugar (paso por referencia)
doblar_valores_en_sitio(mi_lista)
print("Lista después de doblar valores en su lugar:", mi_lista)

# Crear una copia de la lista original y doblar valores (paso por valor)
lista_copiada = doblar_valores_con_copia(mi_lista)
print("Lista original después de la función con copia:", mi_lista)
print("Copia de la lista con valores doblados:", lista_copiada)