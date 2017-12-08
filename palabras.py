import re
def frases(patron, palabra):
    return palabra


if __name__ == "__main__":
    patron = "[t|s|r|8|a|w][a|7|p|r][t|a|o|p]"
    palabra = ["rap them", "tapeth", "apth ", "wrap/try", "sap tray", "87ap9th", "apothecary", "aleht", "happy them", "tarpth", "Apt", "peth", "tarreth", "ddpdg"]


    for palabra in palabra:
        if re.match(patron, palabra):
            print("La palabra", palabra, "cumple con el patron.")
        else:
            print("La palabra", palabra, "no cumple el patron.")

