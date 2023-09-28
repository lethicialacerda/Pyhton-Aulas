numeros = [2,3,5,34,22,18]

opcao = (int(input("Digite um número: ")))
numeros.append(opcao)

print(f'Testando append: {numeros}')

numeros.insert(3, 56)
print(f'Testando insert: {numeros}')

numeros.remove(22)
print(f'Testando remove: {numeros} ')

numeros.pop(2)
print(f'Testando pop: {numeros} ')

numeros.count(2)
print(f'Testando count: {numeros} ')

numeros.copy()
print(f'Testando copy: {numeros} ')

numeros.reverse()
print(f'Testando reverse: {numeros} ')

print(f'{numeros.index(2)}')

numeros.clear()
print(f'Testando clear: {numeros} ')

