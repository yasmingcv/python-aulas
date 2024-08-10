notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(notas[::-1])

#10
print(notas[-1])

#Cópia
lista = notas[:]
print(lista)

#Remove o último se não tiver parametro e retorna o indice do elemento removido
itemRemovido = lista.pop()
print(lista)

#fifo = first in, first out (filas)
#lifo = last in, first out (pilha)

#Exercicio

#elementos = []
# while True:
#     elemento = int(input('Digite um numero pra add na lista ou digite 0 para sair: '))

#     if elemento == 0:
#         montante = 0
#         for e in range(len(elementos)):
#             montante += elementos[e]
#         print(montante/(len(elementos)))
#         break

#     elementos.append(elemento)
#     print(elementos)

