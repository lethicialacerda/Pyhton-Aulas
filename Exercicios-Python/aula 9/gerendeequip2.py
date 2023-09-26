from random import randint
import time

print("Bem vindo ao seu gerenciador de mochila 😉😎")
print(" ")

mochila1 =['Cinzas', 34, 'Capa', 1, 'Poção', 23]
mochila1String = []
mochila1Int = []
mochila2= ['Capa', 2, 'Poção', 3]
mochila2String = []
mochila2Int = []
mochila3= ['Carta', 0]
mochila3String = []
mochila3Int = []


while True:

    print(" ")
    menu =  print('''[1]- Adicionar um item à mochila
[2]- Remover um item da mochila
[3]- Listar todos os itens da mochila
[4]- Sair do programa
\033[31mSelecione uma opção:  \033[0;0m''')

    

    opcao= int(input())

    if (opcao == 1):
        
        while True:
            time.sleep(1)
            print('Você escolheu adicionar um item à mochila, aqui estão as suas opções')
            print("[1] - Mago Dumbledore")
            print("[2] - Bruxo Potter")
            print("[3] - Mago Grindelwald")
            print("[4] - Sair")
            print(" ")
            time.sleep(1)
            opcaoAdicionar = int(input("\033[31mEscolha sua opção: \033[0;0m").strip().capitalize())
            

            if(opcaoAdicionar == 1):
                print(" ")
                time.sleep(1)
                adicioneItem= str(input("Digite o item desejado: ").strip().capitalize())
                quant = randint(0,100)
                print(" ")
                time.sleep(1)
                print(f'Poder do item: {quant}')
                mochila1.append(adicioneItem)
                mochila1.append(quant)
                print(" ")
                time.sleep(1)
                print(f'Lista atualizada:{mochila1}')

            elif(opcaoAdicionar == 2):
                print(" ")
                time.sleep(1)
                adicioneItem= str(input("Digite o item desejado: ").strip().capitalize())
                quant = randint(0,100)
                print(" ")
                time.sleep(1)
                print(f'A quantidade do item é: {quant}')
                mochila2.append(adicioneItem)
                mochila2.append(quant)
                print(" ")
                time.sleep(1)
                print(f'Lista atualizada:{mochila2}')

            elif(opcaoAdicionar == 3 ):
                print(" ")
                time.sleep(1)
                adicioneItem= str(input("Digite o item desejado: ").strip().capitalize())
                quant = randint(0,100)
                print(" ")
                time.sleep(1)
                print(f'A quantidade do item é: {quant}')
                mochila3.append(adicioneItem)
                mochila3.append(quant)
                print(" ")
                time.sleep(1)
                print(f'Lista atualizada:{mochila3}')

            else:
                break
                print(menu)

            
            
    elif (opcao == 2):
        print(" ")
        while True:
            print(" ")
            time.sleep(1)
            print('Você escolheu remover um item à mochila, aqui estão as suas opções de mochila: ')
            print("[1] - Mago Dumbledore")
            print("[2] - Bruxo Potter")
            print("[3] - Mago Grindelwald")
            print("[4] - Sair")
            print(" ")
            time.sleep(1)
            opcaoRemover = int(input("\033[31mEscolha sua opção: \033[0;0m'").strip().capitalize())
            if(opcaoRemover == 1):
                print(mochila1)
                remover = mochila1.pop(int(input("Selecione o objeto a ser removido: ")))
                print(mochila1)
            elif(opcaoRemover == 2):
                print(mochila2)
                remover = mochila2.pop(int(input("Selecione o objeto a ser removido: ")))
                print(mochila2)
            elif(opcaoRemover == 3):
                print(mochila3)
                remover = mochila3.pop(int(input("Selecione o objeto a ser removido: ")))
                print(mochila3)
            else:
                break
                print(menu)

    elif (opcao == 3):

        while True:
            print(" ")
            time.sleep(1)
            print('Escolha uma mochila para ver os itens')
            print("[1] - Mago Dumbledore")
            print("[2] - Bruxo Potter")
            print("[3] - Mago Grindelwald")
            print("[4] - Sair")
            print(" ")
            time.sleep(1)
            opcaoMochila= int(input("\033[31mEscolha a mochila: \033[0;0m")) 


            if(opcaoMochila == 1): 
                print("Itens na mochila: ")
                print(mochila1)
                for valor in mochila1:    
                    if isinstance(valor, str) and valor.strip().isalpha():
                        mochila1String.append(valor)
                    else:
                        mochila1Int.append(valor)

                for i in range(0, len(mochila1Int)):
                    print(f'Item: {mochila1String[i]} Poder: {mochila1Int[i]} ')

                time.sleep(1)
                print('Item de maior poder: ')
                itemPoder = print(max(int(number) for number in  mochila1Int))
            

            elif(opcaoMochila == 2):
                print("Itens na mochila: ")
                print(mochila2)
                for valor in mochila2:    
                    if isinstance(valor, str) and valor.strip().isalpha():
                        mochila2String.append(valor)
                    else:
                        mochila2Int.append(valor)

                for i in range(0, len(mochila2Int)):
                    print(f'Item: {mochila2String[i]} Poder: {mochila2Int[i]} ')

                time.sleep(1)
                print('Item de maior poder: ')
                itemPoder = print(max(int(number) for number in  mochila2Int))

            elif(opcaoMochila == 3):
                print("Itens na mochila: ")
                print(mochila3)
                for valor in mochila3:    
                    if isinstance(valor, str) and valor.strip().isalpha():
                        mochila3String.append(valor)
                    else:
                        mochila3Int.append(valor)

                for i in range(0, len(mochila3Int)):
                    print(f'Item: {mochila3String[i]} Poder: {mochila3Int[i]} ')

                time.sleep(1)
                print('Item de maior poder: ')
                itemPoder = print(max(int(number) for number in  mochila3Int))

            else:
                break
                print(menu)    

    elif (opcao == 4):
        print('Até logo')
        break

    else:
        print("'\033[31mEscolha uma opção entre 1 e 4\033[0;0m'")