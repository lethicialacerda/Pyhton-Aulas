import math

print('*'*50)
print('Bem-vindo')

while True:
    numero = (int(input('Digite um número: ')))
    numeroSoma = numero + numero

    if((numero > 1 and numeroSoma % 2 == 0 )and 
    (numero % 2 != 0 and numero % 3 != 0 )):
        print(f'O número {numero} é um número primo!')
    elif(numero == 2 or numero == 3):
            print(f'O número {numero} é um número primo!')
    else:
        print(f'O número {numero} não é um número primo!')

#esta errado  