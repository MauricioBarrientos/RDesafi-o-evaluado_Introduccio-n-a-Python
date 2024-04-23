print("Cálculo de Utilidades - Versión 1")
print("Ingrese el precio de suscripción:")
P = float(input())
print("Ingrese el número de usuarios:")
U = int(input())
print("Ingrese los gastos totales:")
GT = float(input())

utilidades = P * U - GT

print("Las utilidades son:", utilidades)