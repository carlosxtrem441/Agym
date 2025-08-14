# 4 Pide dos números y muestra el residuo de su división.
'''num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
residuo = num1 % num2
print("El residuo de la división es:", residuo)'''

print("________________________________")

# 9 Pide dos cadenas y verifica si son iguales.
'''cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")  
if cadena1 == cadena2:
    print("Las cadenas son iguales.")   
else:
    print("Las cadenas son diferentes.")'''


print("________________________________")

#Pregunta si llueve y usa not para imprimir si NO está lloviendo.


llueve = input("¿Está lloviendo? (sí/no): ").lower() == "sí"

if not llueve:
    print(" No está lloviendo.")
else:
    print(" Está lloviendo.")