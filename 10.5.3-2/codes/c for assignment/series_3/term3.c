#include <stdio.h>
int main() {
    FILE *file = fopen("data3.txt", "w");
    if (file == NULL) {
        perror("Error");
        return 1;
    }
    float firstTerm = -5;
    float commonDifference = -3;
    int numberOfTerms = 76;
    for (int i = 0; i < numberOfTerms; i++) {
        float term = firstTerm + i * commonDifference;
        fprintf(file, "%f ", term);
    }
    fclose(file);

    return 0;
}

