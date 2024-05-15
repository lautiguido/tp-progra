import random
monedas=55

seguir=True
while seguir:
    juega=input("Juega?s/n")
    if juega=="s":
        apuesta=int(input("su apuesta?"))
        if apuesta>monedas:
            seguir=False
        else:
            seguir=False

seguir=False

