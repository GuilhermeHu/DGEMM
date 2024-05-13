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


# running 1024
# Em (ms) 1024 [81848, 82705, 83211, 89366, 83437, 82757, 83093, 82272, 83064, 82765]
# Em (ms) 1024 [64703, 68375, 61312, 58468, 70171, 62171, 64312, 65781, 66375, 65812]
# média = 83451.8 Desvio padrão = 2019.6867479884102
# média_cpu = 64748.0 Desvio padrão = 3247.890361450029

# running 2048
# Em (ms) 2048 [670588, 676084, 672761, 662531, 668836, 678771, 672856, 661368, 667351, 675614]
# Em (ms) 2048 [551765, 559250, 559640, 547265, 540296, 568640, 559750, 550812, 549046, 552843]
# média = 670676.0 Desvio padrão = 5437.718418601684
# média_cpu = 553930.7 Desvio padrão = 7621.780304495794

# running 4096
# Em (ms) 4096 [20697894, 7211620, 7250955, 7509907, 7405961, 7290199, 7485953, 7459194, 7246334, 7464002]
# Em (ms) 4096 [7566900, 7352173, 7807637, 7256658, 7349559] (extra)
# Em (ms) 4096 [5229406, 6240734, 6335468, 6457968, 6349781, 6232703, 6458578, 6281171, 6025843, 6314812]
# média = 8702201.9 Desvio padrão = 3999964.5132575976
# média_cpu = 6192646.4 Desvio padrão = 341838.8346572695

# 8192
# k = 0 -> t = 69391908
# k = 1 -> t = 69729570
# k = 2 -> t = 73341272
# k = 3 -> t = 70448721
# k = 4 -> t = 69895131
# k = 5 -> t = 71004726
# k = 5 -> t = 70770621
# k = 5 -> t = 72077843
