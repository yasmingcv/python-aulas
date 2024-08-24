qtd = int(input('DIgite a quantidade de termos: '))
valores = [1, 1/3]
pi = 0
sinal = False

for i in range(qtd):
    termo = (-1)**i/(2*i+1)
    pi += 4 * termo

# for valor in valores:
#     if sinal:
#         pi += valor
#         print(sinal, '+')
#         sinal = False
#     else:
#         pi -= valor
#         print(sinal, '-')
#         sinal = True

print(pi)

