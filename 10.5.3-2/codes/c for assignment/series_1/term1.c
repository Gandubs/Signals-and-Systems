#include <stdio.h>
int main() {
    FILE *file = fopen("data1.txt", "w");
    if (file == NULL) {
        perror("Error");
        return 1;
    }
    float firstTerm = 7;
    float commonDifference = 3.5;
    int numberOfTerms = 23;
    for (int i = 0; i < numberOfTerms; i++) {
        float term = firstTerm + i * commonDifference;
        fprintf(file, "%f ", term);
    }
    fclose(file);

    return 0;
}

