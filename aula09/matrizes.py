a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#copia superficialmente
b = a[:]
print(b)

#copia as listas dentro de a, e não referencia
c = [i.copy() for i in a]
print(c)