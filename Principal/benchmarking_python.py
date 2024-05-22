# Going faster 1: Python - benchmarking

import subprocess
import sys
import re
import numpy as np


tamanho_matrizes = [20]
# [1024, 2048, 4096, 8192]

medias = []
medias_cpu = []
for j in tamanho_matrizes:
    runtimes = []
    runtimes_cpu = []
    print("running", j)
    for k in range(2):
        output = subprocess.run(["python", "./DGEMM_1.py", str(j)], capture_output=True, encoding="utf-8", )
        # print(output.stdout, end='')
        lines = output.stdout.split('\n')  # Divide a saída em linhas
        runtimes.append(int(re.findall(r'\d+', lines[0])[0]))  # Captura a primeira linha
        print("k =",k, "-> t =", re.findall(r'\d+', lines[0])[0])
        runtimes_cpu.append(int(re.findall(r'\d+', lines[1])[0]))  # Captura a segunda linha
        sys.stdout.flush()
    print("Em (ms)", j, runtimes)
    print("Em (ms)", j, runtimes_cpu)
    runtimes, runtimes_cpu = np.array(runtimes), np.array(runtimes_cpu)
    medias.append(np.mean(runtimes))
    medias_cpu.append(np.mean(runtimes_cpu))
    print("média =", np.mean(runtimes), "Desvio padrão =", np.std(runtimes))
    print("média_cpu =", np.mean(runtimes_cpu), "Desvio padrão =", np.std(runtimes_cpu))
    print()
print(medias)
print(medias_cpu)
