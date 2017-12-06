Palabra_secreta = "ampoty"
a = 1
#a es igual a un acomulador

print("\ningresa la palabra secreta tienes 3 intentos")
#imprimimos la primera palabra
print("\nte dare la primera pista ")
print("\nes un nombre de usuario de github")
while a < 4:

    print("\n vas por : " + str(a) + " DE 3")
    # me va mostrando en cuanto va mi contador

    palabra = input("PALABRA = ")

    if palabra.lower() == "ampoty":
        print("\nganaste")
        break
    else:
        print("\n enserio lo puedes hacer mejor ")
        a += 1

    if a == 2:
        print("es el usuario de quien siempre utiliza el ejemplo de petra pretof")
    if a == 3:
        print("siempre actualiza los repositorios para que aprendas ")



if a == 4:
    print("perdiste pero tranquilo muchos lo hacen!")