#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

int main(){;
    double N[] = {1E3, 2E3, 5E3, 1E4, 2E4, 5E4, 1E5, 2E5, 5E5, 1E6, 2E6, 5E6};
    int n = 0;
    int *ptr;
    double start, end;
    long long int sum = 0;
    int N_length = 12;
    for(int i = 0; i < N_length; i++){
        n = (int)N[i];
        long double *A = malloc(n * sizeof(long double));
        long double *B = malloc(n * sizeof(long double));
        if(A == NULL || B == NULL){
            printf("Memory allocation failed\n");
            return 1;
        }

        start = omp_get_wtime();
        sum = 0;
        for(int j = 1; j<n; j++){
            A[j] = j;
            B[j] = A[j] * A[j];
            A[j] = A[j] + sqrt(abs(sin(B[j]))) * 2.34;
            sum = sum + A[j];
        }
    end = omp_get_wtime();
    free(A);
    free(B);
    printf("%llu\n", sum);
    printf("%lf\n", end - start);
    }
    
}