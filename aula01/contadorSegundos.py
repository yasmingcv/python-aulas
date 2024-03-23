dias = float(input('dias: '))
horas = float(input('horas: '))
minutos = float(input('minutos: '))

segundos = (dias * 86400) + (horas * 3600) + (minutos * 60)

print(segundos, 'segundos')