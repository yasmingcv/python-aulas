def soma (a, b):
    return a + b

l = [1, 2]
print(soma(*l)) #3

def paramsInfinitos(*params):
    print(params)

paramsInfinitos(1, 2, 3, 4, 5, 6, 7, 8) #(1, 2, 3, 4, 5, 6, 7, 8)

def somaInf(*numeros):
    montante = 0
    for numero in numeros:
        montante += numero
    
    return montante

print(somaInf(2,5,6,7))

#---------------------------------------------------------------------#

qtdElementos = int(input('Digite a quantidade de elementos a serem somados: '))
numeros = []

for i in range(qtdElementos):
    num = int(input(f'Número {i + 1}: '))
    numeros.append(num)

print(somaInf(*numeros))