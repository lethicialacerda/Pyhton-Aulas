'''Leitura de variaveis, o usuário podera
digitar valores. Obs: sempre seram do tipo
String, então terá que converter para uma variavel númerica 
caso seja um número'''

pensamento = input("Meu pensamento: ")
print(pensamento, type (pensamento))

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
r = x + y
print(f"O resultado é: {r}")