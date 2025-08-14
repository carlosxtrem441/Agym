print("_______________________________")
mascota = "perro"
mascota1 = "gato"
print("igual igual", (mascota == mascota1) )# relaciona  si dos variables son identicas 
print("diferente", (mascota != mascota1) )#diferencia
print("mayor",(mascota > mascota1) )#mayor que
print("menor", (mascota < mascota1) )#menor que
print("mayor igual", (mascota >= mascota1) )#mayor igual
print("menor igual", (mascota <= mascota1) )#menor igual

# vamos  a crear 2 usuarios "mascotas"
#nombre 
#especie
#raza
#peso
#color
#edad
#sexo
#dueño
print("____________________________________________________")
def ingresar_mascota(numero):
    print(f"Ingrese los datos de la mascota {numero}:")
    mascota = {}
    mascota["nombre"] = input("Nombre: ")
    mascota["especie"] = input("Especie: ")
    mascota["raza"] = input("Raza: ")
    mascota["peso"] = float(input("Peso: "))
    mascota["color"] = input("Color: ")
    mascota["edad"] = int(input("Edad: "))
    mascota["sexo"] = input("Sexo: ")
    mascota["dueño"] = input("Dueño: ")
    return mascota

mascota1 = ingresar_mascota(1)
mascota2 = ingresar_mascota(2)

print("\nComparación de mascotas:")
for key in mascota1:
    if mascota1[key] == mascota2[key]:
        print(f"{key}: Igual ({mascota1[key]})")
    else:
        print(f"{key}: Diferente ({mascota1[key]} vs {mascota2[key]})")