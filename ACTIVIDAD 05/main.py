# Ejecutar el programa con 3 valores numericos como parametro por consola
import sys

# Obtener la lista de argumentos de la línea de comandos
argumentos = sys.argv

# Verificar si se proporcionaron al menos dos argumentos (nombre del script + al menos un parámetro)
if len(argumentos) < 3:
    print("Uso: python programa.py parametro1 parametro2 [parametro_opcional]")
    sys.exit(1)

# Obtener los parámetros de la línea de comandos
parametro1 = int(argumentos[1])
parametro2 = float(argumentos[2])

# Verificar si se proporcionó un tercer parámetro opcional
parametro_opcional = argumentos[3] if len(argumentos) > 3 else None

# Imprimir los valores de los parámetros
print("Parametro 1:", parametro1)
print("Parametro 2:", parametro2)
print("Opcional:", parametro_opcional)

def funcion_sobrecargada(parametro1, parametro2, *args):
    """
    Función que simula la sobrecarga recibiendo un número variable de parámetros.
    """
    if len(args) == 1:
        resultado = parametro1 * parametro2 * args[0]
    elif len(args) == 2:
        resultado = parametro1 + parametro2 + sum(args)
    else:
        resultado = parametro1 * parametro2

    return resultado

# Ejemplos de llamadas a la función
print(funcion_sobrecargada(5, 3))           # Multiplicación
print(funcion_sobrecargada(2, 3, 4, 5))     # Suma de múltiples valores
print(funcion_sobrecargada(1, 2, 3, 4, 5))  # Producto con múltiples valores