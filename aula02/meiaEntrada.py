idade = int(input('Digite sua idade: '))
carteira = input('Você tem carteira de estudante? (S = sim | N = não): ')

if idade >= 65 or idade <= 21 or carteira.upper() == 'S':
    print('sim')
else:
    print('não')