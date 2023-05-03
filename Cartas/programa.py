cambio_de_nombre = "[nombre]"

with open("../Nombres/nombres.txt", "r") as nombres:
    lista_nombres = nombres.readlines()


with open("../carta_base.txt") as carta_base:
    carta_a_replicar = carta_base.read()
    for nombre in lista_nombres:
        nombre_acortado = nombre.strip()
        nueva_carta = carta_a_replicar.replace(cambio_de_nombre, nombre_acortado)
        with open(f"./../Cartas listas/carta_nueva_{nombre_acortado}.txt", mode="w") as cartas_completas:
            cartas_completas.write(nueva_carta)
