ingreso_user=input("ingrese un usuario")
ingreso_contra=input("ingre un contra")
usuario="domingo"
contraseña="sagra@22"
i=0 #intentos
while i<3:
    ingreso_user=input("ingrese un usuario")
    ingreso_contra=input("ingrese un contra")
    if ingreso_user==usuario and ingreso_contra==contraseña:
        print("bienvenido")
        i=4
    else:
        print("datos no validos")
        i=i+1

