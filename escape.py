import math

print("Cálculo de la Velocidad de Escape")
print("Ingrese el radio en Kilómetros:")
r = float(input())
print("Ingrese la constante g:")
g = float(input())

r = r * 1000  # Convertir el radio a metros
ve = math.sqrt(2 * g)

print("La velocidad de Escape es", ve, "[m/s]")