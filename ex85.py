print("Programa para listar pessoas maiores de idade.")
print("")

nomes = [""] * 7
idades = [0] * 7

for i in range(len(nomes)):
    nomes[i] = input(f"Informe o nome da {i + 1}ª pessoa: ")
    idades[i] = int(input(f"Informe a idade de {nomes[i]}: "))

print("Pessoas com 18 anos ou mais:")

for i in range(len(nomes)):
    if idades[i] >= 18:
        print(nomes[i])