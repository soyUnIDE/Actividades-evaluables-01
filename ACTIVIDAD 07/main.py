import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")

    def es_blue(self):
        if self.color == "blue":
            print("El coche es blue.")

    def matricula_par(self):
        if self.matricula %2 ==0:
            print("La matricula del coche es par.")
        else:
            print("La matricula del coche es impar.")

# Solicitar al usuario un número n por teclado
n = int(input("Ingrese el número de instancias a crear: "))

# Lista de colores disponibles
colores_disponibles = ["red", "white", "black", "pink", "blue"]

# Crear instancias de la clase Car
instancias_cars = []
for i in range(1, n + 1):
    matricula = i
    color = random.choice(colores_disponibles)
    car = Car(matricula, color)
    instancias_cars.append(car)

# Imprimir los valores de las 10 primeras instancias
for i, car in enumerate(instancias_cars[:10]):
    print(f"\nInstancia {i + 1}:")
    car.imprimir()
    car.es_blue()
    car.matricula_par()
