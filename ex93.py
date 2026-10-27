print("Programa para contar vogais, consoantes e outros caracteres.")
print("")


frase = input("Digite uma frase: ")

vogais = 0
consoantes = 0
outros = 0

for caractere in frase.lower():
    if caractere in "aeiou":
        vogais += 1
    elif caractere in "bcdfghjklmnpqrstvwxyz":
        consoantes += 1
    else:
        outros += 1


print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
print(f"Outros caracteres: {outros}")