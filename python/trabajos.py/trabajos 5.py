# 5 Calcula xyx^yxy usando el operador **.
'''base = float(input("Ingrese la base (x): "))
exponente = float(input("Ingrese el exponente (y): "))  
resultado = base ** exponente
print(f"{base} elevado a la {exponente} es:", resultado)'''

print("________________________________")

# 10 Usa operadores relacionales y módulo para determinar si un número es par o impar.
'''numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")'''
    
print("________________________________")

#Determina si un número está entre 10 y 50 y es par al mismo tiempo.

numero = int(input("Ingresa un número: "))

if numero >= 10 and numero <= 50 and numero % 2 == 0:
    print(" El número está entre 10 y 50 y es par.")
else:
    print(" El número no cumple con ambas condiciones.")