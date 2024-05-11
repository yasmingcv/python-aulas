notas = []

while(True):
    nota = input('Digite a nota ou digite "Q" para sair')

    if nota == 'Q':
        break
    else:
        notas.append(int(nota))

total = 0

for i in notas:
    print(i)
    total += i

media = total / len(notas)
print(media)
