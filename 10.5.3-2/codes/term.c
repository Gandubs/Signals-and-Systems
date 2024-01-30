#include <stdio.h>

int main() {
    FILE *file1 = fopen("data1.txt", "w");
    if (file1 == NULL) {
        perror("Error creating file1");
        return 1;
    }
    float x_1 = 7;
    float d_1 = 3.5;
    for (int i = 0; i < 23; i++) {
        float term1 = x_1 + i * d_1;
        fprintf(file1, "%f ", term1);
    }
    fclose(file1);

    FILE *file2 = fopen("data2.txt", "w");
    if (file2 == NULL) {
        perror("Error creating file2");
        return 1;
    }
    float x_2 = 34;
    float d_2 = -2;
    for (int i = 0; i < 13; i++) {
        float term2 = x_2 + i * d_2;
        fprintf(file2, "%f ", term2);
    }
    fclose(file2);

    FILE *file3 = fopen("data3.txt", "w");
    if (file3 == NULL) {
        perror("Error creating file3");
        return 1;
    }
    float x_3 = -5;
    float d_3 = -3;
    for (int i = 0; i < 76; i++) {
        float term3 = x_3 + i * d_3;
        fprintf(file3, "%f ", term3);
    }
    fclose(file3);

    return 0;
}

