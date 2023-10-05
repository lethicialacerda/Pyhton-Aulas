# Atividade 4
# Remova todos os números ímpares da lista a seguir
# [2, 5, 8, 9, 7, 10, 11]

lista = [2, 5, 8, 9, 7, 10, 11]

for i in lista:
    if(i % 2 != 0):
        lista.remove(i)
print(lista)


#outra forma

lista1 = [2, 5, 8, 9, 7, 10, 11]
lista2 = [num for num in lista1 if num % 2 == 0]