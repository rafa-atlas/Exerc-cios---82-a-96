print("Programa para multiplicar os valores de dois vetores.")
print("")

x = [0] * 8
y = [0] * 8

for i in range(len(x)):
    x[i] = int(input(f"Informe o {i + 1}º valor de X: "))

for i in range(len(y)):
    y[i] = int(input(f"Informe o {i + 1}º valor de Y: "))

for i in range(len(x)):
    resultado = x[i] * y[i]
    print(f"{x[i]} x {y[i]} = {resultado}")