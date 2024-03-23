numero = int(input('Digite um número: '))
resto = numero % 2
msg = ''

# msg += 'Par' if resto == 0 else msg += 'Ímpar'

if resto == 0:
    msg += 'Par'
else:
    msg += 'Ímpar'


if numero < 100:
    msg += ' menor que 100'
else: 
    msg += ' maior ou igual a 100'

print(msg)
