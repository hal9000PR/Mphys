#include <stdio.h>
#include <math.h>

int main(){;
    float N = 1000;
    float pi = 0;
    for (int i = 1; i < N + 1; i++) {
        pi += 1 / (1 + pow(((i - 0.5) / N) , 2));
    };
    printf("%f\n", pi * 4 / N);

    return 0;
}