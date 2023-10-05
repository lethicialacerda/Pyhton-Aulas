#atividae 1 - verifique um eterminado número se encontra na seguinte lista:
#[1,3,5,7,11,25,17]
#peça ao usuario digitar um numero, e caso ele estiver na lista
#print a mensagem "Existe"

lista = [1, 3, 5, 7, 11, 25, 17]

escolha = int(input("Digite um número:  "))

for i in lista:
    while escolha == i:
        print("Número já existe na lista")
        break
    