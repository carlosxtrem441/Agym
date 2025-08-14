#_______________________________________
# Listas.En Python
#_______________________________________        
# Listas son colecciones de datos que pueden ser de diferentes tipos
# Listas son mutables, lo que significa que pueden ser modificadas después de su creación
# Listas pueden contener elementos duplicados
# Listas se definen utilizando corchetes []
# Listas pueden contener diferentes tipos de datos, incluyendo números, cadenas, y otras listas
# Listas pueden ser anidadas, es decir, una lista puede contener otras listas
# Listas pueden ser recorridas utilizando bucles for o while
#
frutas = ["manzana", "banana", "cereza", "durazno"]
print (frutas)  # Imprime la lista completa
#___________________________________________________________
#Consultar el dato segun su indice
print(frutas[3])  # Imprime "manzana" (primer elemento)
print(frutas[1])  # Imprime "banana" (segundo elemento)
#____________________________________________________________
#Modificar un elemento de la lista
frutas[2] = "kiwi"  # Cambia "cereza" por "kiwi"
print (frutas)
frutas [3] = "naranja"  # Cambia "durazno" por "naranja"
print (frutas)  # Imprime la lista modificada
#_______________________________________________________
#Agregar un elemento al final de la lista
frutas.append("mango")  # Agrega "mango" al final de la lista
print(frutas)  # Imprime la lista con "mango" agregado
frutas.append("piña")  # Agrega "piña" al final de la lista
print(frutas)  # Imprime la lista con "piña" agregado
#________________________________________________________
#agregar a una posicion especifica
frutas.insert(2, "fresa")  # Agrega "fresa" en
print(frutas)  # Imprime la lista con "fresa" agregado en la posición 2
#________________________________________________________
#Eliminar un elemento de la lista
frutas.remove("banana")  # Elimina "banana" de la lista
print(frutas)  # Imprime la lista sin "banana"
#________________________________________________________
#Eliminar el ultimo elemento de la lista
frutas.pop()  # Elimina el último elemento de la lista (en este caso "
print(frutas)  # Imprime la lista sin el último elemento
#________________________________________________________
#Eliminar un elemento por su indice
frutas.pop (2)  # Elimina el elemento en la posición 2 (en este caso "kiwi")
print(frutas)  # Imprime la lista sin el elemento en la posición 2
#________________________________________________________
#recorrer una lista con un bucle o un ciclo for
for fruta in frutas:  # Recorre cada elemento de la lista
  # Imprime cada fruta en la lista
 print(fruta)  # Imprime cada fruta en la lista
print("las frutas que debemos comer son: ", fruta)  # Imprime un mensaje con cada fruta
#________________________________________________________
 