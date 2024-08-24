import random

matriz = [
    [random.randint(1, 9) for _ in range(7)],
    [random.randint(1, 9) for _ in range(7)],
    [random.randint(1, 9) for _ in range(7)],
    [random.randint(1, 9) for _ in range(7)],
    [random.randint(1, 9) for _ in range(7)],
    [random.randint(1, 9) for _ in range(7)],
    [random.randint(1, 9) for _ in range(7)]
]

for array in matriz:
    for i in array: 
        print(i, end=' ')
    print()