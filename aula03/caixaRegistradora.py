entrada = 1
total = 0
while entrada != 0:
    cod = int(input("informe o codigo do produto"))
    quant = int(input("informe a quantidade comprada"))
    if cod == 1:
        total += quant * 0.50
    elif cod == 2:
        total += quant * 1.0
    elif cod == 3:
        total += quant * 4.0
    elif cod == 5:
        total += quant * 7.0
    elif cod == 9:
        total += quant * 8.0
    else:
        print("opcao inválida")
    entrada = int(input("deseja prosseguir? (1 = sim) (0=nao)"))
print(total)