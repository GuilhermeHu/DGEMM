// Going Faster 5: Cache Blocking (CB)

#include <x86intrin.h>
#include <immintrin.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <math.h>


#define N (size_t)8192
#define UNROLL (4)
#define BLOCKSIZE 32

double A[N][N], B[N][N], C[N][N];

void print_matrix(size_t n, double* A){
  for (size_t i = 0; i < n; i++){   
    for (size_t j = 0; j < n; j++){
      printf("%8.2lf ", A[(i * N) + j]);
    }
    printf("\n");
  }
  printf("\n");
}


void do_block(int n, int si, int sj, int sk, double* A, double* B, double* C){
  for (int i = si; i < si + BLOCKSIZE; i++)
    for (int j = sj; j < sj + BLOCKSIZE; j += 4 * UNROLL) {
      __m256d c[UNROLL];
      for (int r = 0; r < UNROLL; r++)
        c[r] = _mm256_load_pd(C + (i * N) + j + r * 4); //[ UNROLL];

      for (int k = sk; k < sk + BLOCKSIZE; k++)
      {
        __m256d bb = _mm256_broadcast_sd(A + (i * N) + k);
        for (int r = 0; r < UNROLL; r++)
          c[r] = _mm256_add_pd(c[r], _mm256_mul_pd(bb, _mm256_load_pd(B + (N * k) + j + 4 * r)));
      }
      for (int r = 0; r < UNROLL; r++)
        _mm256_store_pd(C + (i * N) + j + r * 4, c[r]);
    }
}

void dgemm(int n, double* A, double* B, double* C){
  for (int si = 0; si < n; si += BLOCKSIZE)
    for (int sj = 0; sj < n; sj += BLOCKSIZE)
      for (int sk = 0; sk < n; sk += BLOCKSIZE)
        do_block(n, si, sj, sk, A, B, C);
}


void make_rand_matrix(size_t n, double* A, int offset) {
    srand(clock() + offset); // Adiciona um deslocamento fixo à semente de aleatoriedade
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            A[i * N + j] = (double)rand() / RAND_MAX * 1000000.0;
        }
    }
}

int main(){

    size_t n;
    printf("Insira o valor de n: ");
    scanf("%zu", &n); 

    LARGE_INTEGER frequency;
    QueryPerformanceFrequency(&frequency);

    double executionTimes[10];
    double totalExecutionTime = 0.0;

    for (int i = 0; i < 10; ++i) {
        make_rand_matrix(n, (double *)A, 0);
        make_rand_matrix(n, (double *)B, 1); // Offset de 1 para garantir valores diferentes para B

        LARGE_INTEGER start, end;
        double executionTime;

        QueryPerformanceCounter(&start);

        dgemm(n, (double *)A, (double *)B, (double *)C);

        QueryPerformanceCounter(&end);

        executionTime = (double)(end.QuadPart - start.QuadPart) / frequency.QuadPart;

        executionTimes[i] = executionTime;
        totalExecutionTime += executionTime;

        // time_t start = clock();
        // dgemm(n, (double *)A, (double *)B, (double *)C);
        // time_t stop = clock();

        // printf("Total time = %ldms\n", (stop - start) * 1000 / CLOCKS_PER_SEC);

        // printf("A =\n");
        // print_matrix(n, (double *)A);
        // printf("B =\n");
        // print_matrix(n, (double *)B);
        // printf("C =\n");
        // print_matrix(n, (double *)C);

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

// gcc -O3 -mavx2 -o DGEMM_5 DGEMM_5.c 
// ./DGEMM_5.exe

// 1024, 2048, 4096, 8192
