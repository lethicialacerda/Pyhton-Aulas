#Exercício jokenpo = o jogador escolhera pedra, papel ou tesoura
# e o computador tambem, atráves da biblioteca random. 18/09/2023

from random import randint
from time import sleep

print('#'*50)
print('Bem-vindo ao jogo do JO-KEN-PO!👊🖐✌')
print("JO-👊")
sleep(1)
print("KEN-🖐")
sleep(1)
print("PO-✌")
sleep(1)

#pontos

acumularPontos = 0

#escolha player
print(' ')
escolhaPlayer = int(input('''Digite: [1]-Pedra👊
[2]-Papel🖐
[3]-Tesoura✌
Sua escolha:  '''))

if(escolhaPlayer == 1):
    print(f'Sua escolha foi: 👊')
elif(escolhaPlayer == 2):
    print(f'Sua escolha foi: 🖐')
elif(escolhaPlayer == 3):
    print(f'Sua escolha foi: ✌')
else:
    print('Reinicie o jogo e escolha uma opção de 1 a 3.')


#Escolha do computador

escolhaComputador = randint(1, 3)

if(escolhaComputador == 1):
    sleep(1)
    print(f'A escolha do computador foi: 👊')
elif(escolhaComputador == 2):
    sleep(1)
    print(f'A escolha do computador foi: 🖐')
else:
    sleep(1)
    print(f'A escolha do computador foi: ✌')


if((escolhaPlayer == 1 and escolhaComputador == 3)or 
   (escolhaPlayer == 2 and escolhaComputador == 1)or
   (escolhaPlayer == 3 and escolhaComputador == 2)):
    print('Parabéns você ganhou!!')
    acumularPontos = acumularPontos + 1
elif(escolhaPlayer == escolhaComputador):
    print('Empate!')
else:
    print('Você perdeu, Game over')        

