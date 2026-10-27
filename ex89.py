print("Programa para somar e multiplicar valores de um vetor.")
print("")

valores = [0] * 10

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}º número: "))

soma = 0
multiplicacao = 1

for i in range(len(valores)):
    if i % 2 == 0:
        multiplicacao *= valores[i]
    else:
        soma += valores[i]

print(f"Soma das posições ímpares: {soma}")
print(f"Multiplicação das posições pares: {multiplicacao}")