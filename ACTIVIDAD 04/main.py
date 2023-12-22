# Ejemplo de operador "is"
a = [1, 2, 3]
b = a  # b apunta al mismo objeto que a

if a is b:
    print("a y b son el mismo objeto en memoria.")
else:
    print("a y b no son el mismo objeto en memoria.")

# Ejemplo de operador "not"
valor = False

# not hace que el booleano pase a su contrario si estaba en False pasa a True y lo mismo al reves
if not valor:
    print("La condición es verdadera.")
else:
    print("La condición es falsa.")

# Ejemplo de operador "in"
lista_numeros = [1, 2, 3, 4, 5]

numero_buscar = 3

# in su usa para listas y es una traduccion literal, basicamente "si x EN lista" devuelve true y si no está devuelve false
if numero_buscar in lista_numeros:
    print(f"{numero_buscar} está en la lista.")
else:
    print(f"{numero_buscar} no está en la lista.")