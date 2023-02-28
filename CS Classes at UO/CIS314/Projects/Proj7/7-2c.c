#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct ColorPoint {
     long a;
     long r;
     long g;
     long b;
};

long f(struct ColorPoint **points, int n) {
     long sum = 0;
     for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
             sum += points[j][i].a;
             sum += points[j][i].r;
             sum += points[j][i].g;
             sum += points[j][i].b;
        }
    }
    return sum;
}

long g(struct ColorPoint **points, int n) {
     long sum = 0;
     for (int i = 0; i < n; i++) {
         for (int j = 0; j < n; j++) {
             sum += points[i][j].a;
             sum += points[i][j].r;
             sum += points[i][j].g;
             sum += points[i][j].b;
        }
    }
    return sum;
}

struct ColorPoint** create2DArray(int n) {
     // Array to hold a pointer to the beginning of each row
     struct ColorPoint **points =
     (struct ColorPoint **)malloc(n * sizeof(struct ColorPoint *));
     for (int i = 0; i < n; ++i) {
         // Array to hold each row
         points[i] =
         (struct ColorPoint *)malloc(n * sizeof(struct ColorPoint));
         for (int j = 0; j < n; ++j) {
             // Init the ColorPoint struct
             points[i][j].a = rand();
             points[i][j].r = rand();
             points[i][j].g = rand();
             points[i][j].b = rand();
        }
    }
    return points;
}

void free2DArray(struct ColorPoint** points, int n) {
     for (int i = 0; i < n; ++i) {
        free(points[i]);
     }
     free(points);
}

int main() {
    int size = 2048;
    struct ColorPoint **points = create2DArray(size);
    int num1 = 0;
    
    clock_t start = clock();
    // Do this 1000 times to exaggerate the time taken.
    for (int i = 0; i < 1000; i++) {
        f(points, num1);
    }
    clock_t end = clock();
    double totalTime1 = ((double) (end - start)) / CLOCKS_PER_SEC;
    
    start = clock();
    // Do this 1000 times to exaggerate the time taken.
    for (int i = 0; i < 1000; i++) {
        g(points, num1);
    }
    end = clock();
    double totalTime2 = ((double) (end - start)) / CLOCKS_PER_SEC;
    
    free2DArray(points, num1);
    
    printf("f: %f\n", totalTime1);
    printf("g: %f\n", totalTime2);
}
