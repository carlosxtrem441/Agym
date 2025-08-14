#FORMULARIO
print("FORMULARIO")
print("POR FAVOR , COMPLETA LOS SIGUIENTES FORMULARIO")
nombre = input("Ingrese su nombre: ")
print("ingrese su edad:")
edad = int(input())
print("ingrese:", nombre, edad," años")
#crear un formulario de presentacion  en el cual el usuario ingrese sus datos por consola
#debe implementar  datos tipo  string,entero,float,booleano,
print("formulario de presentacion")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura: "))
print("¿Eres estudiante? (si/no): ")
es_estudiante = input().strip().lower() == 'si'
print(f"Hola, mi nombre es {nombre} {apellido}, tengo {edad} años, "
      f"mi estatura es {estatura} metros y {'soy' if es_estudiante else 'no soy'} estudiante.")
