import numpy as np
from time import perf_counter

n = int(input("Dimensão da matriz: "))

l = []
for i in range(10):
    # Gerando matrizes aleatórias
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    time_start = perf_counter()
    # Multiplicação das matrizes
    C = np.dot(A, B)
    time_end = perf_counter()

    # print("Matriz A:")
    # print(A)
    # print("\nMatriz B:")
    # print(B)
    # print("\nResultado da multiplicação:")
    # print(C)

    l.append(time_end - time_start)
    print("Total time = %f ms" % ((time_end - time_start)*1000))

print()
print(np.array(l))
print("Media: ", np.mean(l))
print("Desvio padrão: ", np.std(l))
