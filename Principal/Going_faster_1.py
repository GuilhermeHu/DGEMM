# Going Faster 1: Python


import sys, time, random
from time import perf_counter


# tamanho da matriz
n = int(sys.argv[1])
# n = 200

# Geração de matrizes aleatórias
A = [[random.random() for _ in range(n)] for _ in range(n)]
B = [[random.random() for _ in range(n)] for _ in range(n)]
C = [[0 for _ in range(n)] for _ in range(n)]


def DGEMM(A, B, C):
  for i in range(n):
    for j in range(n):
      for k in range(n):
        C[i][j] += A[i][k] * B[k][j]


def main():

  # Geração de matrizes aleatórias
  A = [[random.random() for _ in range(n)] for _ in range(n)]
  B = [[random.random() for _ in range(n)] for _ in range(n)]
  C = [[0 for _ in range(n)] for _ in range(n)]

  time_start, time_start_cpu = 0, 0
  time_start, time_start_cpu = perf_counter(), time.process_time()
  DGEMM(A,B,C)
  time_end, time_end_cpu = perf_counter(), time.process_time()

  print("Total time = %fms" % ((time_end - time_start)*1000))
  print("Total time = %fms" % ((time_end_cpu - time_start_cpu)*1000))
  # print("Total time = %f s" % (time_end - time_start))
  # print("A = ", A)
  # print("B = ", B)
  # print("C = ", C)

main()
