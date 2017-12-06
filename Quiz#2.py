class Figu:
    def Cono(self):
        r = float(input("digite la el radio: "))
        a = float(input("digite la altura: "))
        Volumen1 = ((r ** 2 * a) / 3) * 3.141592
        print("El volumen del cono es:", "{0:.2f}".format(Volumen1))

    def Cilindro(self):
        r = float(input("Ingrese el radio: "))
        a = float(input("Ingrese la altura: "))
        Volumen2 = 3.141592 * r ** 2 * a
        print("El volumen del cilindro es:", "{0:.2f}".format(Volumen2))

    def Esfera(self):
        r = float(input("Ingrese el radio: "))
        Volumen3 = (4 / 3) * 3.141592 * r ** 3
        print("El volumen de la esfera es: ", "{0:.2f}".format(Volumen3))


class CEsfera(Figu):
    def formula(self):
        self.Esfera()


class CCilindro(Figu):
    def formula(self):
        self.Cilindro()


class CCono(Figu):
    def formula(self):
        self.Cono()


if __name__ == "__main__":
    print("Opciones\n1. Esfera   2. Cilindro  3. Cono")
    Opcion = int(input('Que opcion desea utilizar: '))

    try:
        if Opcion == 1:
            CEsfera().formula()
        elif Opcion == 2:
            CCilindro().formula()
        elif Opcion == 3:
            CCono().formula()
    except:print("opcion no valida.")