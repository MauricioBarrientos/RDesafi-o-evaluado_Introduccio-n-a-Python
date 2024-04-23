print("Cálculo de Utilidades - Versión 3")
print("Ingrese el precio de suscripción:")
P = float(input())
print("Ingrese el número de usuarios normales:")
U = int(input())
print("Ingrese los gastos totales:")
GT = float(input())
print("Ingrese las utilidades del año anterior:")
Uanterior = float(input())

utilidades = P * U - GT
razon_utilidades = utilidades / Uanterior

print("Las utilidades son:", utilidades)
print("La razón entre las utilidades actuales y las del año anterior es:", round(razon_utilidades, 2))