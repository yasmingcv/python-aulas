def somaListas(a,b):
    total = []

    i = 0

    for i in range(len(a)):
        total.append(a[i] + b[i])
        
    
    return total

print(somaListas([2,2,3], [3,2,1]))