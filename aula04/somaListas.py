def somaListas(a,b):
    total = []

    i = 0

    while i < len(a):
        total.append(a[i] + b[i])
        i += 1
    
    return total

print(somaListas([1,2,3], [3,2,1]))