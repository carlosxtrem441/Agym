#tipos de opreradores en python
#operadores aritméticos
print("operadores aritméticos")
numero1 = 10
numero2 = 5
print("suma:", numero1 + numero2)
print("resta:", numero1 - numero2)
print("multiplicación:", numero1 * numero2) 
print("división:", numero1 / numero2)
print("módulo:", numero1 % numero2)
print("exponente:", numero1 ** numero2)
print("división entera:", numero1 // numero2)
print("===============================")
#crear una calculadora simple que tenga las funciones de arriba
print("calculadora simple")
def calculadora_simple(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        return a / b if b != 0 else "Error: División por cero"
    elif operacion == "modulo":
        return a % b
    elif operacion == "exponente":
        return a ** b
    elif operacion == "division_entera":
        return a // b if b != 0 else "Error: División por cero"
    else:
        return "Operación no válida"
    
op = input("Ingrese la operación (suma, resta, multiplicacion, division, modulo, exponente, division_entera): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
resultado = calculadora_simple(num1, num2, op)
print("Resultado:", resultado)
