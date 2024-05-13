# Going Faster 1: Python


import sys, time, random
from time import perf_counter # benchmarking: https://superfastpython.com/benchmark-time-perf-counter/


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



# # CASOS TESTES
# # 3 matrizes de inteiros -> 2^1, 2^2, 2^3
# # 3 matrizes de float ->  2^1, 2^2, 2^3

# k2_liv_int , k2_num_int = [[],0],[[],0]
# k4_liv_int , k4_num_int = [[],0],[[],0]
# k8_liv_int , k8_num_int = [[],0],[[],0]

# k2_liv_flo , k2_num_flo = [[],0],[[],0]
# k4_liv_flo , k4_num_flo = [[],0],[[],0]
# k8_liv_flo , k8_num_flo = [[],0],[[],0]

# l =[k2_liv_int , k2_num_int ,
#     k4_liv_int , k4_num_int ,
#     k8_liv_int , k8_num_int ,
#     k2_liv_flo , k2_num_flo ,
#     k4_liv_flo , k4_num_flo ,
#     k8_liv_flo , k8_num_flo ]

# s =["k2_liv_int" , "k2_num_int" ,
#     "k4_liv_int" , "k4_num_int" ,
#     "k8_liv_int" , "k8_num_int" ,
#     "k2_liv_flo" , "k2_num_flo" ,
#     "k4_liv_flo" , "k4_num_flo" ,
#     "k8_liv_flo" , "k8_num_flo" ]

# def multimat (n,m):
#     # Criando matrizes aleatórias
#     # if m == 0:
#     #     A = np.random.randint(0,  2**9, (n, n))    # m=0 -> operação com matriz de inteiros
#     #     B = np.random.randint(0,  2**9, (n, n))    # m=1 -> operação com matriz de float
#     # else:
#     #     A = np.random.rand(n, n)
#     #     B = np.random.rand(n, n)
#     # Criando matrizes aleatórias
#     if m == 0:
#         for i in range(n):
#             for j in range(n):
#                 A[n][n] = 
#                 B[n][n] =
#     else:
#         A = np.random.rand(n, n)
#         B = np.random.rand(n, n)

#     C,D = [],[]
#     for i in range(n): 
#         C.append([0]*n)
#         D.append([0]*n)


#     time_start = perf_counter()
#     # alteração 1: livro usa xrange, mas isso era coisa do Python 2. Diz o chatgpt que o range do python 3 tem mesma eficiencia
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 C[i][j] += A[i][k] * B[k][j]
#     time_end = perf_counter()
#     time_duration_1 = time_end - time_start
#     # print(f'C took {time_duration_1:.3f} seconds')
#     # print(C)
        
#     time_start = perf_counter()
#     D = np.dot(A, B)
#     time_end = perf_counter()
#     time_duration_2 = time_end - time_start
#     # print(f'D took {time_duration_2:.3f} seconds')
#     # print(D)
#     return time_duration_1, time_duration_2

# def distribuicao(a,b, x, c):
#     if c==0:
#         if x == 1:
#             k2_liv_int[0].append(a)
#             k2_num_int[0].append(b)
#             k2_liv_int[1] += a
#             k2_num_int[1] += b
#         elif x==2:
#             k4_liv_int[0].append(a)
#             k4_num_int[0].append(b)
#             k4_liv_int[1] += a
#             k4_num_int[1] += b
#         elif x==3:
#             k8_liv_int[0].append(a)
#             k8_num_int[0].append(b)
#             k8_liv_int[1] += a
#             k8_num_int[1] += b
#     elif c==1:
#         if x == 1:
#             k2_liv_flo[0].append(a)
#             k2_num_flo[0].append(b)
#             k2_liv_flo[1] += a
#             k2_num_flo[1] += b
#         elif x==2:
#             k4_liv_flo[0].append(a)
#             k4_num_flo[0].append(b)
#             k4_liv_flo[1] += a
#             k4_num_flo[1] += b
#         elif x==3:
#             k8_liv_flo[0].append(a)
#             k8_num_flo[0].append(b)
#             k8_liv_flo[1] += a
#             k8_num_flo[1] += b
    
                            
# n = int(input())
# N=10
# print("Numeros float:                      Livro  /  Numpy")
# while N != 0:
#     # for ...
#     # print("Numeros inteiros:                   Livro  /  Numpy")

#     # a,b = multimat(n,0)
#     # distribuicao(a,b,n/2000,0)
#     # print(f'{8}k entradas =          {a} / {b}')
#     # # vdd => 1000 * (2**(x+3))
#     # # teste => 10 * (x+3)
        
#     # print("Numeros float:                      Livro  /  Numpy")
#     a,b = multimat(n,1)
#     distribuicao(a,b,n/2000,1)
#     print(f'{n/1000}k entradas =          {a} / {b}')

#     N-=1

# # for e in range(len(l)):
# #     print(s[e])
# #     print(l[e][0])
# #     print("Media = ", l[e][1]/10, "s")
# #     print()
    
# if n == 2000:
#     for i in range(2):
#         print(s[i])
#         print(l[i][0])
#         print("Media = ", l[i][1]/10, "s")
# elif n==4000:
#     for i in range(2):
#         print(s[i+2])
#         print(l[i+2][0])
#         print("Media = ", l[i+2][1]/10, "s")
# elif n==8000: 
#     for i in range(2):
#         print(s[i+4])
#         print(l[i+4][0])
#         print("Media = ", l[i+4][1]/10, "s")