from datetime import date

diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year

diaNascimento = int(input('Dia do nascimento:'))
mesNascimento = int(input('Mês do nascimento: '))
anoNascimento = int(input('Ano do nascimento: '))

if(mesNascimento == mesAtual):
    print('Estou no mês de aniversário')
    if(diaNascimento == diaAtual):
        print('Hoje é dia do meu aniversário')
        idade = anoAtual - anoNascimento
        print(f'Minha idade é: {idade}')
    elif(diaNascimento < diaAtual):
        print('já fiz aniversário')
        idade = anoAtual - anoNascimento
        print(f'Minha idade é: {idade}')
    else:
        print('Ainda não fiz anivrsário mas estou no mês')
        idade = (anoAtual - anoNascimento)-1
        print(f'Minha idade é: {idade}')    

elif(mesNascimento < mesAtual):
    print('O mês de nascimento é menor que o mês atual')
    print('Ja fiz aniversário 🎈')
    idade = anoAtual - anoNascimento
    print(f'Minha idade é: {idade}') 
    
else:
    print('O mês de nascimento é menor que o mês atual')  
    print('Não fez aniversario 😐')  
    idade = (anoAtual - anoNascimento)-1
    print(f'Minha idade é: {idade}') 

'''if(anoAtual - anoNascimento >= 18 and mesNascimento - mesAtual <= 0 and diaNascimento - diaAtual <= 0):
    print('Liberado!')
else:
    print('Negado')  
'''
      



