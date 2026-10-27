valores = [0] * 11
for i in range(len(valores)):
     valores[i] = int(input(f"Informe o {i + 1}ª valor: "))

for i in range(len(valores)):
     print(valores[i])
     print("-" * 20)