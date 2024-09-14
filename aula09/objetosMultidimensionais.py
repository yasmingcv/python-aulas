import matplotlib.pyplot as plt

# black = 255
# white = 0
# isblack = True

# xadrez = []

# for i in range(9):
#     linha = []
#     for j in range(9):
#         rgb = []
#         for k in range(3):
#             rgb.append(black if isblack == 0 else white)
#         isblack = not isblack
#         linha.append(rgb)
#     xadrez.append(linha)

linha = 8
coluna = 8
xadrez = [[[255*((i+j)%2), 255*((i+j)%2), 255*((i+j)%2)] for i in range(coluna) ] for j in range(linha)]

print(xadrez)
plt.imshow(xadrez)
plt.axis('off')
plt.show()