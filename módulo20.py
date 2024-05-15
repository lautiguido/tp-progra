m = int(input("Ingrese el primer número (m): "))
n = int(input("Ingrese el segundo número (n): "))

if n < m:
    print("Error: El segundo número (n) debe ser mayor o igual que el primer número (m).")
else:
    cont = m
    while cont <= n:
        print(cont, end=" ")
        cont += 1
