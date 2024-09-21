listaDeCompras = ['biscoito', 'chocolate', 'farinha']

supermercado = {
    'amaciante': 4.99,
    'arroz': 10.90,
    'biscoito': 1.69,
    'cafe': 6.98,
    'chocolate': 3.79,
    'farinha': 2.99
}

total = 0
for i in listaDeCompras:
    if i in supermercado:
        total += supermercado[i]

print(total)