# Imprime un mensaje indicando que se mostrarán los pares de números con un ciclo
print("Pares de números entre", m, "y", n, "con un ciclo:")
# Inicializa la variable i con el valor de m
i = m
# Utiliza un ciclo while para iterar sobre los números desde m hasta n (incluyendo n)
while i <= n:
    # Inicializa la variable j con el valor de m
    j = m
    # Utiliza un ciclo while para iterar sobre los números desde m hasta n (incluyendo n)
    while j <= n:
        # Imprime el par de números i y j
        print(i, j)
        # Incrementa j en 1 para pasar al siguiente número
        j += 1
    # Incrementa i en 1 para pasar al siguiente número
    i += 1