import random
numero_a_seleccionar=int(input("ingrese un numero del 0 a 99"))
monto_a_apostar=float(input("ingrese un monto a apostar"))
numero_de_la_suerte=random.randint(0,99)
if numero_a_seleccionar==numero_de_la_suerte:
    premio=monto_a_apostar*70
    print("felicidades usted gano",premio,"pesos")
else:
    print("usted fallo vuelva a intentarlo")
    print("el numero de la suerte era:",numero_de_la_suerte)