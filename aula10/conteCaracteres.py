frase = 'Os ratossssssssssssssssss'
dicionario = {}

for letra in frase:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1
    

print(dicionario)