print("Programa para contar ocorrências de um número.")
print("")

x = int(input("Informe o número X: "))
valores = [0] * 32

for i in range(len(valores)):
    valores[i] = int(input(f"Informe o {i + 1}º número: "))

quantidade = 0

for numero in valores:
    if numero == x:
        quantidade += 1

print(f"O número {x} aparece {quantidade} vezes.")