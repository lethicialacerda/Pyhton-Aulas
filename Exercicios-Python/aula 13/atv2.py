# Atividade 2 
# Contar números positivos da lista a seguir:
# [2, -3, -1, 4, 0, -9]

lista = [2, -3, -1, 4, 0, -9]

numPositivos = 0


for i in lista:
    if(i > 0):
        numPositivos += 1
        print(f'{i} é um número positivo')
print(f'Há {numPositivos} números positivos na lista')
        
  
  
