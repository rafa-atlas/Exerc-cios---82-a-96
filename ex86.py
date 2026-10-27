print("Programa para contar quantas vezes um número aparece no vetor.")
print("")

valores = [0] * 10

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}º número: "))

x = int(input("Informe o número X: "))

quantidade = 0

for numero in valores:
    if numero == x:
        quantidade += 1

print(f"O número {x} aparece {quantidade} vezes.")