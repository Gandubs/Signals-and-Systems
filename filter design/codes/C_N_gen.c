#include <stdio.h>
#include <math.h>

int main() {
    double w, x, c_N;
    FILE *file;

    file = fopen("cn_values.txt", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    for (w = 0; w <= 2.0; w += 0.01) {
        x = w / 1.0; // Assuming w_Lp is 1
        if (x <= 1) {
            c_N = cos(4 * acos(x)); // Using 4 directly
        } else {
            c_N = cosh(4 * acosh(x)); // Using 4 directly
        }
        fprintf(file, "%.2f %.8f\n", w, c_N);
    }

    fclose(file);
    printf("Values of C_N written to cn_values.txt\n");

    return 0;
}

