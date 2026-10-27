print("Programa para separar números pares e ímpares.")
print("")

valores = [0] * 12

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}º número: "))
pares = []
impares = []

for numero in valores:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")