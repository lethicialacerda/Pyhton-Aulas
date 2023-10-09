listaNumero = [1,2,3,4,5,6,7,8,9,10]
subLista = []
subListaNumero = 3

for i in range(0,len(listaNumero), subListaNumero):
    subListap = listaNumero[i:i + subListaNumero]
    subLista.append(subListap)
print(subLista)

#outra for de fazer sublistas

subListaForma = [[]for _ in range(3)]
listaA = [1,2]
listaB = [3,4,5]
listaC = [6,7,8,9]
subListaForma[0].extend(listaA)
subListaForma[0].extend(listaB)
subListaForma[0].extend(listaC)
print(subListaForma)

#lista do luigi

a = []
a.append(listaA)
a.append(listaB)
a.append(listaC)
print(a)

#outra forma de fazer
listaOutra = [1,2,3,4,5,6]
subListaP1 = listaOutra[2:len(listaOutra)-1]
print(subListaP1)
