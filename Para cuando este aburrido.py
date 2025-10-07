s = 
while s == 0:    
    while Tru:
        try:
            num_multiplicar = float(input("Tabla de multiplicar que quiera: "))
            break
        except ValueError:
            print("Es un numero, no una letra")

    for i in range(1,11):
        resultado = num_multiplicar * i
        print(f"El resultado de multiplicar {num_multiplicar} por {i} es igual a {resultado}")
        i += 1

s = input("desea volver a repetir el programa (S/N):")
