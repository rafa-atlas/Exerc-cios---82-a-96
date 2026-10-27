print("Programa para calcular a média das notas dos alunos.")
print("")

nomes = [""] * 5
notas = [0.0] * 5

for i in range(len(nomes)):
    nomes[i] = input(f"Informe o nome do {i + 1}º aluno: ")
    notas[i] = float(input(f"Informe a nota de {nomes[i]}: "))

media = sum(notas) / len(notas)

print(f"A média das notas é {media}.")
print("Alunos com nota menor que 7:")

for i in range(len(nomes)):
    if notas[i] < 7:
        print(nomes[i])