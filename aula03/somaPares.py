inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))
soma = 0

while inicio <= fim:
    if inicio % 2 == 0:
        soma += inicio
    
    inicio += 1

print(soma)