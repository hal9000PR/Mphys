#include <stdio.h>
#include <math.h>

int main(){;
    int N = 10;
    int i = 0;
    float pi = 0;
    for (i = 1; i < N + 1; i++) {
        pi += 1 / (1 + pow(((i - 1/2) / N) , 2));
    };
    printf("%f\n", pi * 4/N);

    return 0;
}