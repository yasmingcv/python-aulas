fila = []

while True:
    acao = input('Digite A para adicionar na fila ou R para remover da fila: ')


    if acao == 'A':
        nome = input('Digite o nome da pessoa: ')
        fila.append(nome)
    elif acao == 'R':
        rem = fila.pop(0)
        print(f'{rem} foi atendido')
        print(f'o tamanho da fila é de {len(fila)} pessoas')
    
    print(fila)
    cont = input('Deseja cotinuar? (S/N)')

    if cont == 'N':
        break
