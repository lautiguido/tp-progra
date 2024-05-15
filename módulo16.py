import random

# Generar el número de la suerte al azar entre 0 y 99
numero_suerte = random.randint(0, 99)

# Inicializar un contador para llevar el registro de los intentos
intentos = 0

while True:
    # Incrementar el contador de intentos en cada iteración
    intentos = intentos+ 1

    # Solicitar al usuario que ingrese su número y el monto a apostar
    numero_apostado = int(input("Intento {}: Ingrese su número entre 0 y 99 (o -1 para salir): ".format(intentos)))

    # Salir del bucle si el usuario ingresa -1
    if numero_apostado == -1:
        print("Gracias por jugar. ¡Hasta luego!")
        break

    monto_apostado = float(input("Ingrese el monto a apostar: "))

    # Verificar si el usuario acertó el número
    if numero_apostado == numero_suerte:
        # Calcular las ganancias si el usuario acierta
        ganancias = monto_apostado * 70
        print("¡Felicidades! Acertaste el número de la suerte:", numero_suerte)
        print("Ganaste", ganancias, "veces tu apuesta.")
        break
    else:
        print("Lo siento, el número de la suerte era:", numero_suerte)
        print("Inténtalo de nuevo.")
