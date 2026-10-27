print("Programa para substituir caracteres inválidos por traços.")
print("")


frase = input("Digite uma frase: ")


resultado = ""

for caractere in frase:
    if caractere.lower() in "abcdefghijklmnopqrstuvwxyz":
        resultado += caractere
    else:
        resultado += "-"


print(f"Resultado: {resultado}")