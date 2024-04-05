#include <stdio.h>


void generate_Y(double x[], double y[]) {
    x[-1]=0;
    y[0] = x[0];
    for (int n = 1; n < 20; n++) {
        y[n] = x[n] + x[n - 2] - 0.5 * y[n - 1];
    }
}

int main() {
    double x[20] = {1, 2, 3, 4, 2, 1};
    double y[20];

    generate_Y(x, y);

    FILE *fp = fopen("y_n_output.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Writing y[n] values to the file
    for (int i = 0; i < 20; i++) {
        fprintf(fp, "%.6f\n", y[i]);
    }

    fclose(fp);
    printf("Data written to y_n_output.txt successfully.\n");
    return 0;
}

