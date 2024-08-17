import matplotlib.pyplot as plt

x = []
for i in range(101):
    x.append(i * 6 / 100)

y = []    
def verifica(x):
    if(x < 2):
        y.append(1)
    elif(x <= 3.5):
        y.append(2)
    elif(x < 5):
        y.append(3)
    else:
        y.append((x**2)-10*x+28)

for i in x:
    verifica(i)

plt.plot(x, y, marker = 'o', linestyle='dotted')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Titulo')
plt.grid(True)
plt.show()


