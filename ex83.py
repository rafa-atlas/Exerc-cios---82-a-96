print("Programa para exibir 18 números em ordem inversa.")
print("")

valores = [0] * 18

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}º valor: "))

for i in range(len(valores) - 1, -1, -1):
    print(valores[i])