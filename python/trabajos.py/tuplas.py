#_______________________________________________________________
#TUPLAS EN Python
#_______________________________________________________________
# Tuplas son colecciones de datos que pueden ser de diferentes tipos
# Tuplas son inmutables, lo que significa que no pueden ser modificadas después de su creació  
# Tuplas pueden contener elementos duplicados
# Tuplas se definen utilizando paréntesis ()    
# Tuplas pueden contener diferentes tipos de datos, incluyendo números, cadenas, y otras tuplas
# Tuplas pueden ser anidadas, es decir, una tupla puede contener otras tuplas
# crear una tupla
jugadores =("FALCAO", "CR7", "MESSI", "NEYMAR", "MBAPPE",  "JAMES", "QUINTERO", "OSPINA")
print(jugadores)  # Imprime la tupla completa
#___________________________________________________________
#Consultar el dato segun su indice
print(jugadores[0])  # Imprime "FALCAO" (primer elemento)
print(jugadores[4])  # Imprime "CR7" (segundo elemento)
print(jugadores[7])  # Imprime "OSPINA" (octavo elemento)
#___________________________________________________________
#las tuplas son inmutables, no se pueden modificar
#jugadores[2] = "MESSI"  # Esto generará un error porque las tuplas no se pueden modificar
#___________________________________________________________
#RECORRER UNA TUPLA CON UN BUCLE O UN CICLO FOR
for jugador in jugadores:  # Recorre cada elemento de la tupla
    print("La alineación del partido es",)  # Imprime cada jugador en la tupla
    print(jugador)  # Imprime cada jugador en la tupla
#___________________________________________________________
#si queremos modificar una tupla debemos crear una nueva tupla
nueva_alineacion = jugadores + ("YERRY MINA",)  # Agrega "YERRI MINA" a la tupla
print(nueva_alineacion)  # Imprime la nueva tupla con "YERRY MINA" agregado
#___________________________________________________________    
#DESEMPAQUETAR UNA TUPLA
FALCAO, CR7, MESSI, NEYMAR, MBAPPE, JAMES, QUINTERO, OSPINA = jugadores
print ("FALCAO", FALCAO)  # Imprime "FALCAO"
print ("CR7", CR7)  # Imprime "CR7"
print ("MESSI", MESSI)  # Imprime "MESSI"
print ("NEYMAR", NEYMAR)  # Imprime "NEYMAR"
print ("MBAPPE", MBAPPE)  # Imprime "MBAPPE"
#_______________________________________________________________