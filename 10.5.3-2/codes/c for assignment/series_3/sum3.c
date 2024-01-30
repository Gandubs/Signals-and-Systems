#include <stdio.h>
int main() {
    FILE *file = fopen("data3.txt", "r");
    if (file == NULL) {
        perror("Error");
        return 1;
    }
    float term, sum = 0.0;
    while (fscanf(file, "%f", &term) == 1) {
        sum += term;
    }
    fclose(file);
    printf("Sum : %.1f\n", sum);

    return 0;
}

