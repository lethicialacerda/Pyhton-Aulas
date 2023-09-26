import math

altura = (float(input("Digite sua altura: ")))
peso = (float(input("Digite seu peso: ")))

expAltura = (math.pow(altura, 2))
print(f"Seu imc é: {peso/expAltura}")