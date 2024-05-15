import random
i=True
contador=0
suma=0

while i==True:
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    suma=suma+dado1+dado2
    print(dado1,"--",dado2,"--",suma)
    if dado1==dado2:
        i=False
    contador=contador+1
print("necesito",suma,"para que los dados sean iguales")


