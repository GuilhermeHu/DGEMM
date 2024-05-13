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


# 1024, 2048, 4096, 8192

# PS C:\Users\guilh\OneDrive\VScode\Arq comp> & C:/Users/guilh/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/guilh/OneDrive/VScode/Arq comp/DGEMM_np.py"
# Dimensão da matriz: 1024
# Total time = 17.092000 ms
# Total time = 14.307300 ms
# Total time = 14.186700 ms
# Total time = 14.731000 ms
# Total time = 14.587800 ms
# Total time = 14.431900 ms
# Total time = 14.172000 ms
# Total time = 14.426900 ms
# Total time = 13.867600 ms
# Total time = 14.077100 ms

# [0.017092  0.0143073 0.0141867 0.014731  0.0145878 0.0144319 0.014172
#  0.0144269 0.0138676 0.0140771]
# Media:  0.014588030031882226
# Desvio padrão:  0.0008679671878462762
# PS C:\Users\guilh\OneDrive\VScode\Arq comp> & C:/Users/guilh/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/guilh/OneDrive/VScode/Arq comp/DGEMM_np.py"
# Dimensão da matriz: 2048
# Total time = 125.743300 ms
# Total time = 106.426400 ms
# Total time = 106.006800 ms
# Total time = 106.224900 ms
# Total time = 106.374800 ms
# Total time = 107.222000 ms
# Total time = 106.425400 ms
# Total time = 112.154000 ms
# Total time = 106.971300 ms
# Total time = 106.755200 ms

# [0.1257433 0.1064264 0.1060068 0.1062249 0.1063748 0.107222  0.1064254
#  0.112154  0.1069713 0.1067552]
# Media:  0.10903041001874954
# Desvio padrão:  0.005825776177398836
# PS C:\Users\guilh\OneDrive\VScode\Arq comp> & C:/Users/guilh/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/guilh/OneDrive/VScode/Arq comp/DGEMM_np.py"
# Dimensão da matriz: 4096
# Total time = 946.343600 ms
# Total time = 983.441500 ms
# Total time = 920.491000 ms
# Total time = 883.469400 ms
# Total time = 878.662700 ms
# Total time = 883.225100 ms
# Total time = 893.050100 ms
# Total time = 883.100700 ms
# Total time = 876.929200 ms
# Total time = 890.536000 ms

# [0.9463436 0.9834415 0.920491  0.8834694 0.8786627 0.8832251 0.8930501
#  0.8831007 0.8769292 0.890536 ]
# Media:  0.9039249299792573
# Desvio padrão:  0.03367743822460992
# PS C:\Users\guilh\OneDrive\VScode\Arq comp> & C:/Users/guilh/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/guilh/OneDrive/VScode/Arq comp/DGEMM_np.py"
# Dimensão da matriz: 8192
# Total time = 6887.880200 ms
# Total time = 6889.614100 ms
# Total time = 6777.255900 ms
# Total time = 6929.172100 ms
# Total time = 6932.200900 ms
# Total time = 6942.673900 ms
# Total time = 6940.351800 ms
# Total time = 7521.104800 ms
# Total time = 7306.044000 ms
# Total time = 7388.056200 ms

# [6.8878802 6.8896141 6.7772559 6.9291721 6.9322009 6.9426739 6.9403518
#  7.5211048 7.306044  7.3880562]
# Media:  7.051435390021652
# Desvio padrão:  0.24086782528556858