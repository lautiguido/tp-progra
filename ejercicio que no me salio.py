import random
monedas=25
suma=0

while monedas<=25:
    apuesta=int(input("ingrese un numero"))
    dado1= 6 #random.randint(1,6)
    dado2=4 #random.randint(1,6)
    print(dado1,dado2)
    if dado1==dado2:
        monedas=monedas+apuesta*2
        print("usted gano",apuesta*2,"y tiene",monedas)
    else:
        monedas=monedas-apuesta
        print("y tiene",monedas)





