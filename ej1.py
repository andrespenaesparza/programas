
suma_positivos = 0
suma_negativos = 0
cantidad_ceros = 0


for i in range(1, 6):
    numero = int(input(f"Ingrese el número {i}: "))

    if numero > 0:
        suma_positivos += numero
    elif numero < 0:
        suma_negativos += numero
    else:
        cantidad_ceros += 1
        print("Se ingresó un cero.")


print("\nResultados:")
print("Suma de positivos:", suma_positivos)
print("Suma de negativos:", suma_negativos)
print("Cantidad de ceros:", cantidad_ceros)
