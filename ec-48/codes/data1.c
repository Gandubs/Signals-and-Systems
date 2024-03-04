#include <stdio.h>
#include <gsl/gsl_poly.h>

int main(void) {
    int i, j;
    double kp, ki;
    double a[5]; // Coefficients array for a 4th degree polynomial
    double z[8]; // Complex roots array

    // Open the file for writing
    FILE *fp = fopen("data.txt", "w");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Redirect stdout to the file
    if (freopen("data.txt", "w", stdout) == NULL) {
        perror("freopen() failed");
        return 1;
    }

    for (i = 0; i <= 20; i++) {
        kp = -1.0 + 0.5 * i; // Range for kp: -1 to 9 with a space of 0.5

        for (j = 0; j <= 28; j++) {
            ki = 0.0 + 0.125 * j; // Range for ki: 0 to 3.5 with a space of 0.125

            // Calculate coefficients
            a[0] = 2 * ki;
            a[1] = 2 + 2 * kp;
            a[2] = 5;
            a[3] = 4;
            a[4] = 1;

            // Allocate memory for GSL polynomial complex workspace
            gsl_poly_complex_workspace *w = gsl_poly_complex_workspace_alloc(5);

            // Solve polynomial equation
            gsl_poly_complex_solve(a, 5, w, z);

            // Free GSL polynomial complex workspace
            gsl_poly_complex_workspace_free(w);

            // Write the roots to the file
            fprintf(fp, "For kp = %f and ki = %f:\n", kp, ki);
            for (int k = 0; k < 4; k++) {
                fprintf(fp, "Root %d: %+.18f %+.18f\n", k + 1, z[2 * k], z[2 * k + 1]);
            }
            fprintf(fp, "\n");
        }
    }

    // Close the file
    fclose(fp);

    return 0;
}
