vetA = [[1,2],
        [3,4],
        [5,6]]

vetB = [[1, 2, 3],
        [4, 5, 6]]


matrizResultado = []
for linha in range(0, len(vetA)):
    for coluna in range(0, len(vetB)):
        print(f'linha {vetA[linha]} coluna {vetB[coluna]}')
   