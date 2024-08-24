def prodInt(qtd):
    lista1 = []
    lista2 = []
    produto = 0
    for i in range(qtd):
        lista1.append(i)
        lista2.append(i + 2)
        produto += lista1[i] * lista2[i]

    return produto

print(prodInt(10))
