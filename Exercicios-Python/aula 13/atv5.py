# Atividade: Manipulação de Listas em Python (sem funções)

nomes = ["Alice", "Bob", "Carol", "David", "Eva"]

sublista_nomes = nomes[1:4]
print(sublista_nomes)

for nome in nomes:
    print(nome)

nome_a_procurar = "Emily"
if nome_a_procurar in nomes:
    print(nome_a_procurar, "está na lista.")
else:
    print(nome_a_procurar, "não está na lista.")

letra_a_contagem = sum(1 for nome in nomes if nome.startswith("A"))
print("Número de nomes que começam com 'A':", letra_a_contagem)


#Atividade Append

lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublista = []

indice_inicio = 2  # O índice de início da sublista
indice_fim = 6    # O índice de fim da sublista

for i in range(indice_inicio, indice_fim + 1):
    sublista.append(lista_original[i])
print("Sublista:", sublista)
