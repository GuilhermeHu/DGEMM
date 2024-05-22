// Going faster 2: C (puro e suas otimizações -O1, -O2 e -O3)


#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>

#define N ((size_t)8192)
// size_t max = 4294967295

double A[N][N], B[N][N], C[N][N];


void dgemm (int n, double* A, double* B, double* C) {
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) {
            for( int k = 0; k < n; k++ )
                C[(i * N) + j] += A[(i * N) + k] * B[(k * N) + j];  
    }
}


void printMatrix(double* matrix, size_t n) {
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            printf("%8.2lf ", matrix[(i * N) + j]);
        }
        printf("\n");
    }
    printf("\n");
}

void make_rand_matrix(size_t n, double A[][N], double B[][N]){
    srand(GetTickCount());
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            A[i][j] = (double)rand() / RAND_MAX * 1000000.0; 
            B[i][j] = (double)rand() / RAND_MAX * 1000000.0; 
        }
    }
}

int main() {
    // Defina o tamanho das matrizes
    size_t n;
    printf("Insira o valor de n: ");
    scanf("%zu", &n);

    LARGE_INTEGER frequency;
    QueryPerformanceFrequency(&frequency);

    double executionTimes[10];
    double totalExecutionTime = 0.0;

    for (int i = 0; i < 10; ++i) {
        make_rand_matrix(n, A, B);

        LARGE_INTEGER start, end;
        double executionTime;

        QueryPerformanceCounter(&start);

        // Chama a função de multiplicação de matriz
        dgemm(n, (double *)A, (double *)B, (double *)C);

        QueryPerformanceCounter(&end);

        // Calcula o tempo de execução em segundos
        executionTime = (double)(end.QuadPart - start.QuadPart) / frequency.QuadPart;

        executionTimes[i] = executionTime;
        totalExecutionTime += executionTime;

        // printMatrix((double *)A, n);
        // printMatrix((double *)B, n);
        // printMatrix((double *)C, n);

        printf("Tempo de execucao do ciclo %d: %f segundos\n", i + 1, executionTime);
    }

    double mean = totalExecutionTime / 10.0;

    double sumSquaredDiff = 0.0;
    for (int i = 0; i < 10; ++i) {
        sumSquaredDiff += pow(executionTimes[i] - mean, 2);
    }
    double standardDeviation = sqrt(sumSquaredDiff / 10.0);

    printf("Media dos tempos de execucao: %f segundos\n", mean);
    printf("Desvio padrao dos tempos de execucao: %f segundos\n", standardDeviation);

    return 0;
}


// gcc -o DGEMM DGEMM_2.c -m64
// gcc -o DGEMM_2 -O1 DGEMM_2.c -m64
// gcc -o DGEMM_2 -O2 DGEMM_2.c -m64
// gcc -o DGEMM_2 -O3 DGEMM_2.c -m64
// ./DGEMM_2.exe

// 1024, 2048, 4096, 8192
