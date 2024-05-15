import random
i=True
contador=0
suma=0
while i==True:
    dado_1=random.randint(1,6)
    dado_2=random.randint(1,6)
    suma=suma+dado_1+dado_2
    print(dado_1,"--",dado_2,"suma:",suma)
    if suma>100:
        i=False
    contador=contador+1

print("necesito",contador,"tiradas para....>100")

