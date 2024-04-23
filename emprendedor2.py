print("Cálculo de Utilidades - Versión 2")
print("Ingrese el precio de suscripción:")
P = float(input())
print("Ingrese el número de usuarios normales:")
Unormal = int(input())
print("Ingrese el número de usuarios premium:")
Upremium = int(input())
print("Ingrese los gastos totales:")
GT = float(input())

Ppremium = P * 1.5  # Precio de suscripción para usuarios premium
U = Unormal + Upremium
utilidades = P * Unormal + Ppremium * Upremium - GT

print("Las utilidades son:", utilidades)