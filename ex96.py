print("Programa para trocar caracteres de posição.")
print("")


valores = [""] * 12

for i in range(len(valores)):
    valores[i] = input(f"Informe o {i + 1}º caractere: ")


for i in range(0, len(valores), 2):
    temporario = valores[i]
    valores[i] = valores[i + 1]
    valores[i + 1] = temporario


print(f"Vetor após as trocas: {valores}")