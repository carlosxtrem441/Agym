
print("hola mi nombre es :")
print("carlos andres jimenez bermudez")
print("sede donde estudio:")
print("centro de servicios finacieros")
print("tecnologo en desarrollo de software")

mensaje = 'hola mundo'
mensaje_mayusculas = mensaje.upper()
print(mensaje_mayusculas)

mensaje_minusculas = mensaje.lower()
print(mensaje_minusculas)
#formato de cadena 
var_color = 'rojo'
var_edad = '28'
# Imprimir los valores 
print(var_color, var_edad)
#Concatenacion de cadenas (unir dos o mas cadenas, +)
var_color = 'rojo'+ ' ' + var_edad
print("color",var_color)
#Interpolacion de cadenas, usando la letra f
var_color = f'mi cadena: {var_color} {var_edad}'
print("color", var_color)
#Interpolacion con multilineas f'' '''
print(f''' mi cadena: 
      {var_color}
        {var_edad}''')