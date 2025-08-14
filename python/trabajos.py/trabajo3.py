# 3 Calcula el área de un triángulo con base y altura ingresadas por el usuario.
'''base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))  
area = (base * altura) / 2  
print("El área del triángulo es:", area)'''

print("________________________________")

# 8 Ingresa una calificación y verifica si es mayor o igual a 3.0.
'''calificacion = float(input("Ingrese la calificación: "))
if calificacion >= 3.0:
    print("La calificación es aprobatoria.")
else:
    print("La calificación no es aprobatoria.")'''

print("________________________________")

# 13 Pide tres valores booleanos e imprime si al menos uno es True (usa or).

valor1 = input("Ingresa el primer valor (True/False): ") == "True"
valor2 = input("Ingresa el segundo valor (True/False): ") == "True"
valor3 = input("Ingresa el tercer valor (True/False): ") == "True"


if valor1 or valor2 or valor3:
    print(" Al menos uno de los valores es True.")
else:
    print(" Ninguno de los valores es True.")