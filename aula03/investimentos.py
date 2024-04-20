depositoInicial = float(input('Digite o valor do depósito inicial: '))
taxaDeJuros = float(input('Digite a taxa de juros: '))
depositoMensal = float(input('Digite o depósito mensal: '))
periodo = int(input('Digite o período em meses: '))
montante = depositoInicial
i = 1

while i < periodo:
    rendimentoMensal = (depositoMensal + montante ) / 100 * taxaDeJuros

    montante += depositoMensal + rendimentoMensal

    print(f'Mês {i}: {montante}')  
    i += 1