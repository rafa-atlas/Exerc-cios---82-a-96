print("Programa para encontrar valores comuns entre dois vetores.")
print("")

x = [0] * 10
y = [0] * 12

for i in range(len(x)):
    x[i] = int(input(f"Informe o {i + 1}º valor do primeiro vetor: "))

for i in range(len(y)):
    y[i] = int(input(f"Informe o {i + 1}º valor do segundo vetor: "))

comuns = []

for numero in x:
    if numero in y and numero not in comuns:
        comuns.append(numero)

comuns.sort(reverse=True)

print(f"Valores comuns em ordem decrescente: {comuns}")