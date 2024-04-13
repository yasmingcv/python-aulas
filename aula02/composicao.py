nome = 'Maria'
idade = 25
salario = 4650.37

#composicao antiga - % e a letra correspondente ao tipo da variavel, float (.2f) formata quantas casas decimais terá
msg = '%s tem %d anos e ganha R$%.2f' % (nome, idade, salario)
print(msg)

#versao 2 do python
msg2 = '{:-^20s} tem {} anos e ganha R${:.2f}'.format(nome, idade, salario)
print(msg2)

#nova forma
msg3 = f'{nome:*^15s} tem {idade} anos e ganha R${salario:.1f}'
print(msg3)