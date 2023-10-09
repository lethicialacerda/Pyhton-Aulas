dicionario = {
    "nome1":"paulo",
    "nome2":"Ana",
    "nome3": "João"
}

valor = dicionario["nome1"]
print(valor)

dicionario["nome4"]="Julieta"
valor = dicionario["nome4"]
print(valor)

for chave,valor in dicionario.items():
    print(f'Chave {chave} e valor é {valor}')