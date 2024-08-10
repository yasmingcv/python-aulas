n = int(input('Digite um número: '))

# for i in range(altura):
#         print(' ' * (altura - i), end='')
#         print('*' * (2 * i + 1))


# for i in range(n):
#     print(f'{'*' * (2 * i + 1):^{2 * n - 1}}')

#-------------------------arvore inversa-------------------------#
count = n
while count > 0:
    print(' ' * ( n - count ), end='')
    print('*' * (count * 2 - 1))
    count -= 1