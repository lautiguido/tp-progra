m=int(input("ingrese un numero"))
n=int(input("ingrese un numero"))
if n < m:
    print("Error: El segundo número (n) debe ser mayor o igual que el primer número (m).")
else:
    cont = m
    while cont<=n:
        cont=cont+1
        print(cont)

