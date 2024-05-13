// Double precision GEneral Matrix Multiply

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


// gcc -o DGEMM_2_manual DGEMM_2_manual.c -m64
// gcc -o DGEMM_2_manual -O1 DGEMM_2_manual.c -m64
// gcc -o DGEMM_2_manual -O2 DGEMM_2_manual.c -m64
// gcc -o DGEMM_2_manual -O3 DGEMM_2_manual.c -m64
// ./DGEMM_2_manual.exe

// 1024, 2048, 4096, 8192


// PS C:\Users\guilh\OneDrive\VScode\Arq comp> gcc -o DGEMM_2_manual -O2 DGEMM_2_manual.c -m64
// PS C:\Users\guilh\OneDrive\VScode\Arq comp> ./DGEMM_2_manual.exe
// Insira o valor de n: 8192
// Tempo de execucao do ciclo 1: 6525.520926 segundos
// Tempo de execucao do ciclo 2: 6523.784752 segundos
// Tempo de execucao do ciclo 3: 6526.391652 segundos
// Tempo de execucao do ciclo 4: 6528.198951 segundos
// Tempo de execucao do ciclo 5: 6523.503289 segundos
// Tempo de execucao do ciclo 6: 6523.308745 segundos
// Tempo de execucao do ciclo 7: 6524.828911 segundos
// Tempo de execucao do ciclo 8: 6525.745575 segundos
// Tempo de execucao do ciclo 9: 6526.619499 segundos
// Tempo de execucao do ciclo 10: 6523.379687 segundos
// Media dos tempos de execucao: 6525.128199 segundos
// Desvio padrao dos tempos de execucao: 1.571231 segundos



//  CÓDIGO QUE FUNCIONA

// // Double precision GEneral Matrix Multiply

// #include <stdio.h>
// #include <stdlib.h>
// #include <windows.h>
// #include <math.h>

// #define N ((size_t)8192)
// // size_t max = 4294967295

// double A[N][N], B[N][N], C[N][N];


// // void dgemm (int n, double* A, double* B, double* C) {
// //     for (int i = 0; i < n; ++i)
// //         for (int j = 0; j < n; ++j) {
// //             double cij = C[i+j*n]; /* cij = C[i][j] */
// //             for( int k = 0; k < n; k++ )
// //                 cij += A[i+k*n] * B[k+j*n]; /* cij += A[i][k]*B[k][j] */
// //             C[i+j*n] = cij; /* C[i][j] = cij */
// //     }
// // }

// void dgemm(size_t n, double A[][N], double B[][N], double C[][N]) {
//     for (size_t i = 0; i < n; ++i)
//         for (size_t j = 0; j < n; ++j) {
//             double cij = C[i][j];
//             for (size_t k = 0; k < n; k++)
//                 cij += A[i][k] * B[k][j];
//             C[i][j] = cij;
//         }
// }

// void printMatrix(double* matrix, size_t n) {
//     for (size_t i = 0; i < n; ++i) {
//         for (size_t j = 0; j < n; ++j) {
//             printf("%8.2lf ", matrix[(i * N) + j]);
//         }
//         printf("\n");
//     }
//     printf("\n");
// }

// void make_rand_matrix(size_t n, double A[][N], double B[][N]){
//     srand(GetTickCount());
//     for (size_t i = 0; i < n; ++i) {
//         for (size_t j = 0; j < n; ++j) {
//             A[i][j] = (double)rand() / RAND_MAX * 1000000.0; 
//             B[i][j] = (double)rand() / RAND_MAX * 1000000.0; 
//         }
//     }
// }

// int main() {
//     // Defina o tamanho das matrizes
//     size_t n;
//     printf("Insira o valor de n: ");
//     scanf("%zu", &n);

//     LARGE_INTEGER frequency;
//     QueryPerformanceFrequency(&frequency);

//     double executionTimes[10];
//     double totalExecutionTime = 0.0;

//     for (int i = 0; i < 10; ++i) {
//         make_rand_matrix(n, A, B);

//         LARGE_INTEGER start, end;
//         double executionTime;

//         QueryPerformanceCounter(&start);

//         // Chama a função de multiplicação de matriz
//         dgemm(n, A, B, C);

//         QueryPerformanceCounter(&end);

//         // Calcula o tempo de execução em segundos
//         executionTime = (double)(end.QuadPart - start.QuadPart) / frequency.QuadPart;

//         executionTimes[i] = executionTime;
//         totalExecutionTime += executionTime;

//         // printMatrix((double *)A, n);
//         // printMatrix((double *)B, n);
//         // printMatrix((double *)C, n);

//         printf("Tempo de execucao do ciclo %d: %f segundos\n", i + 1, executionTime);
//     }

//     double mean = totalExecutionTime / 10.0;

//     double sumSquaredDiff = 0.0;
//     for (int i = 0; i < 10; ++i) {
//         sumSquaredDiff += pow(executionTimes[i] - mean, 2);
//     }
//     double standardDeviation = sqrt(sumSquaredDiff / 10.0);

//     printf("Media dos tempos de execucao: %f segundos\n", mean);
//     printf("Desvio padrao dos tempos de execucao: %f segundos\n", standardDeviation);

//     return 0;
// }