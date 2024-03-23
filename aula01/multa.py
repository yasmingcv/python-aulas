velocidade = float(input('digite a velocidade do carro: '))

if velocidade > 80:
    print('MULTADO!!!!!! R$', (velocidade - 80) * 5, 'de multa')
else:
    print('nao')