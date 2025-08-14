#Ejercicios con listas
#_______________________________________
#Crea una lista con 5 productos de supermercado y muéstrala en pantalla.
productos = ["leche", "pan", "huevos", "queso", "manzanas"]
print(productos)
#_______________________________________
#Tienes una lista con 4 comidas favoritas, cambia la segunda por un nuevo platillo.
comidas_favoritas = ["pizza", "sushi", "tacos", "pasta"]
print(comidas_favoritas)
comidas_favoritas[1] = "Camarones"  # Cambia "sushi" por "Pollo asado
print(comidas_favoritas)
#Crea una lista con 3 invitados a una fiesta, agrega dos más, y luego elimina uno.
invitados = ["diego", "brayan", "laura"]
print(invitados)
invitados.append("Ingrid")
invitados.append("Maryury")
print(invitados)
invitados.remove("diego")
print(invitados)
#_______________________________________
#Crea una lista con 5 colores y muestra la lista en orden inverso usando reverse() o [::-1].
colores = ["rojo", "azul", "verde", "amarillo", "naranja","morado"]
print(colores)
colores.reverse()  # Usando reverse()
print(colores)
#_______________________________________
#Crea una lista con animales y usa len() para mostrar cuántos hay.
animales = ["perro", "gato", "pez", "pájaro", "conejo"]
print(animales)
print("Número de animales en la lista:", len(animales))
animales.append("hamster")
print(animales)
print("Número de animales en la lista:", len(animales))
#_______________________________________
#Crea una lista con elementos repetidos y usa set() para mostrar la lista sin duplicados.
elementos = ["Automovil", "Bicicleta", "Avion", "Barco", "Bicicleta", "Avion"]
print(elementos)
elementos_sin_duplicados = list(set(elementos))  # Usando set() para eliminar duplicados
print(elementos_sin_duplicados)
#_______________________________________
#Crea una lista de números y genera una nueva lista con el cuadrado de cada número
#usando un bucle o comprensión de listas.
numeros = [1, 2, 3, 4, 5]
print (numeros)
cuadrados =[x**2 for x in numeros]  # Usando comprensión de listas
print(cuadrados)
#_______________________________________
#Une dos listas (por ejemplo, jugadores y posicion) en una sola y muéstrala.
jugadores = ["FALCAO", "CR7", "MESSI", "OSPINA"]
print(jugadores)
posiciones = ["Delantero", "Volante", "Creador", "Portero"]
print(posiciones)
equipo = jugadores + posiciones  # Uniendo dos listas
print
#_______________________________________# ...existing code...
jugadores = ["FALCAO-", "CR7-", "MESSI-", "OSPINA-"]
print(jugadores)
posiciones = ["DELANTERO", "VOLANTE", "CREADOR", "PORTERO"]
print(posiciones)
equipo = list(zip(jugadores, posiciones))  # Emparejando jugadores con posiciones
 
for jugador, posicion in equipo:
    print(jugador, posicion)
#_______________________________________
#De una lista de números, elimina todos los que sean menores a 5.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros)
numeros_filtrados = [num for num in numeros if num >= 5]  # Filtrando números mayores o iguales a 5
print(numeros_filtrados)
print(numeros)
#Crea una lista que represente el inventario de una tienda. Permite que el usuario agregue
#y quite productos mediante input().
inventario = ["zapatos", "camisetas", "pantalones", "gorras"]
print("Inventario inicial:", inventario)
while True:
    accion = input("¿Deseas agregar o quitar un producto? (agregar/quitar/salir): ").strip().lower()
    if accion == "agregar":
        producto = input("Ingresa el producto a agregar: ")
        inventario.append(producto)
        print(f"Producto '{producto}' agregado. Inventario actual: {inventario}")
    elif accion == "quitar":
        producto = input("Ingresa el producto a quitar: ")
        if producto in inventario:
            inventario.remove(producto)
            print(f"Producto '{producto}' quitado. Inventario actual: {inventario}")
        else:
            print(f"El producto '{producto}' no está en el inventario.")
    elif accion == "salir":
        print("Saliendo del programa.")
        break
    else:
        print("Acción no válida. Por favor, ingresa 'agregar', 'quitar' o 'salir'.")