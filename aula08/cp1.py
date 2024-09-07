def lerMatriz(l, c):
    matriz = []
    linha = []

    for j in range(l):
        linha = []
        for i in range(c):
            linha.append(int(input(f'Matriz[{j}][{i}]: ')))
        matriz.append(linha)
    return matriz

def subMatrizes(m1, m2):
    if(len(m1) == len(m2) and len(m1[0]) == len(m2[0])):
        c = []
        for j in range(len(m1)):
            linha = []
            for i in range(len(m1[0])):
                linha.append(m1[j][i] - m2[j][i])
            c.append(linha)
        
        return c
    else:
        print('tamanhos diferentes')

def transpostaMatriz(matriz):
    trans = []
    for j in range(len(matriz[0])):
        linha = []
        for i in range(len(matriz)):
            linha.append(matriz[i][j])
            print(matriz[i][j])
        trans.append(linha)
    return trans

def matrizEsparsa(matriz):
    qtdZero = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                qtdZero += 1
    return qtdZero > ((len(matriz) * len(matriz[0]))/2)

print(matrizEsparsa(
    [
        [0,3],
        [0,1],
        [0,1],
        [0,1]
    ]
))
