#include <stdio.h>
#include <math.h>

int main(){;
    float N;
    printf("INPUT 1 INTEGER:  ");
    scanf("%f", &N);
    float pi = 0;
    for (int i = 1; i < N + 1; i++) {
        pi += 1 / (1 + pow(((i - 0.5) / N) , 2));
    };
    printf("RESULT:  ");
    printf("%f\n", pi * 4 / N);
    scanf("%f", &N);

    return 0;
}