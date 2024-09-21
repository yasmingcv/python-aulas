qtd = int(input('Digite a quantidade de usuários a serem adicionados: '))
users = {}

for i in range(qtd):
    nome = input('Nome: ')
    idade = input('Idade: ')
    sexo = input('Sexo: ')

    users[nome] = [idade, sexo]

print(users)