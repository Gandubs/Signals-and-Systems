#include <stdio.h>

int main() {
    FILE *file1 = fopen("data1.txt", "r");
    if (file1 == NULL) {
        perror("Error opening data1.txt");
        return 1;
    }
    float term1, sum1 = 0.0;
    while (fscanf(file1, "%f", &term1) == 1) {
        sum1 += term1;
    }
    fclose(file1);
    printf("Sum for x_1(n): %.1f\n", sum1);

    FILE *file2 = fopen("data2.txt", "r");
    if (file2 == NULL) {
        perror("Error opening data2.txt");
        return 1;
    }
    float term2, sum2 = 0.0;
    while (fscanf(file2, "%f", &term2) == 1) {
        sum2 += term2;
    }
    fclose(file2);
    printf("Sum for x_2(n): %.1f\n", sum2);

    FILE *file3 = fopen("data3.txt", "r");
    if (file3 == NULL) {
        perror("Error opening data3.txt");
        return 1;
    }
    float term3, sum3 = 0.0;
    while (fscanf(file3, "%f", &term3) == 1) {
        sum3 += term3;
    }
    fclose(file3);
    printf("Sum for x_3(n): %.1f\n", sum3);

    return 0;
}

