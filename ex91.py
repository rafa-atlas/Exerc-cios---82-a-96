print("Programa para identificar números ímpares.")
print("")


valores = [0] * 21

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}º número: "))


impares = []

for numero in valores:
    if numero % 2 != 0:
        impares.append(numero)

impares.sort()

if len(impares) == 0:
    print("Todos são pares.")
else:
    print("Existem números ímpares.")
    print(f"Números ímpares em ordem crescente: {impares}")

