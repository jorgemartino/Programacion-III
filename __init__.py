print("Bienvenidos")
nombre = input("ingrese su nombre porfavor")
archivo = open("preguntasYrespuestas.txt","r")
linea1 = archivo.readline()
print (linea1)
rlinea2 = input ("coloque la respuesta aqui:")
linea2 = archivo.readline()
print("la respuesta es:"+ linea2 )
if linea2 == rlinea2:
    print("Correcto")
else: print("incorrecto")

linea3 = archivo.readline()
print (linea3)
rlinea4 = input ("coloque la respuesta aqui:")
linea4 = archivo.readline()
print("la respuesta es:"+ linea4 )
if linea4 == rlinea4:
    print("Correcto")
else: print("incorrecto")

linea5 = archivo.readline()
print (linea5)
rlinea6 = input ("coloque la respuesta aqui:")
linea6 = archivo.readline()
print("la respuesta es:"+ linea6 )
if linea6 == rlinea6:
    print("Correcto")
else: print("incorrecto")

linea7 = archivo.readline()
print (linea7)
rlinea8 = input ("coloque la respuesta aqui:")
linea8= archivo.readline()
print("la respuesta es:"+ linea8 )
if linea8 == rlinea8:
    print("Correcto")
else: print("incorrecto")
archivo.close()