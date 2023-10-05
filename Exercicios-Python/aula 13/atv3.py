# Atividade 3
# Verifique se a lista está em ordem crescente:
# [1, 2, 3, 5, 7, 10]
#caso positivo, retorne uma mensagem

lista = [1, 2, 3, 5, 7, 10]

if(sorted(lista) == lista):
    print('Lista está em ordem crescente')
else:
    print('Lista não está em ordem crescente')
