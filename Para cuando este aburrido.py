while True:
    try:
        # Pide el número para la tabla
        num_multiplicar = float(input("Tabla de multiplicar que quiera: "))

        # Genera la tabla del 1 al 10
        for i in range(1, 11):
            resultado = num_multiplicar * i
            print(f"El resultado de multiplicar {num_multiplicar} por {i} es igual a {resultado}")

        # Pregunta si desea repetir
        s = input("¿Desea volver a repetir el programa (S/N)?: ").strip().upper()

        # Si no responde S, el programa termina
        if s != "S":
            print("Programa finalizado.")
            break

    except ValueError:
        print("Es un número, no una letra.")
