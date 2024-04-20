numNotas = int(input('Digite a quantidade de notas: '))
media = 0
i = 0

while i < numNotas:
    media += int(input(f'Digite a nota {i+1}: '))
    i += 1

media = media / numNotas

print(media)