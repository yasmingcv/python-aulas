kwh = int(input('Digite a quantidade de kWh consumida: '))
tipo = input('''
Digite o tipo de instalação:
R - residências
I - industrias
C - comércios
 ''')
preco = 0
continua = True


if tipo.upper() == 'R':
    if kwh < 500:
        preco = kwh * 0.4
    else:
        preco = kwh * 0.65
elif tipo.upper() == 'C':
    if kwh < 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.6
elif tipo.upper() == 'I':
    if kwh < 5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.6
else:
    print('Opção inválida!')
    continua = False

if continua:
    print(preco)
    
