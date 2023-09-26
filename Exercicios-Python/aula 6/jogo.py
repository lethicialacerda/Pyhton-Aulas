from random import randint

print('-'*105)
print(f'Escolha uma opção: \n [1]-ímpar \n [2]-par')

escolha = int(input())
   
#minha resolução

if(escolha == 1):
    print('Sua escolha foi: ímpar')
    print('Escolha um número: ')
    numero1 = int(input())
    print('Escolha da máquina: ')
    numero2 = randint(0, 100)
    print(numero2)
    if((numero1+numero2)%2 == 0):
        print('Máquina ganhou!🤖')
    else:
        print('Você ganhou!😃')

if(escolha == 2):
    print('Sua escolha foi: par')
    print('Escolha um número: ')
    numero1 = int(input())
    print('Escolha da máquina: ')
    numero2 = randint(0, 100)
    print(numero2)
    if((numero1+numero2)%2 == 0):
        print('Você ganhou!😃')
    else:
        print('Máquina ganhou!🤖')
     
