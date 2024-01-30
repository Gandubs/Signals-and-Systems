#include <stdio.h>
int main() {
    FILE *file = fopen("data2.txt", "w");
    if (file == NULL) {
        perror("Error");
        return 1;
    }
    float firstTerm = 34;
    float commonDifference = -2;
    int numberOfTerms = 13;
    for (int i = 0; i < numberOfTerms; i++) {
        float term = firstTerm + i * commonDifference;
        fprintf(file, "%f ", term);
    }
    fclose(file);

    return 0;
}

