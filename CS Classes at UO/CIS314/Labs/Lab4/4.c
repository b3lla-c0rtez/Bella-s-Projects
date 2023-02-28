#include <stdio.h>
#include <stdlib.h>

int readInt() {
        char lineBuf[10];
        char *p = NULL;
        int n;

        while (1) {
                // char* fgets (char* str, int num, FILE* stream);
                fgets(lineBuf, sizeof(lineBuf), stdin);

                // long int strtol (const char* str, char** endptr, int base);
                n = strtol(lineBuf, &p, 10);
                if (lineBuf != p) {
                        break;
                }

                printf("Invalid input\nPlease enter a valid array value: ");
        }

        return n;
}

int main() {
        // to do:

        // create int array of fixed length
        
        // call stack is a data structure program execution and local variables
        // implemented as a stack(obviously)
        // "set in stone"
    
        // heap is a different data structure that manages dynamically allocated memory
        // list of addresses: 0x1, 0x2, ... up to "RAM Size", commonly implemented as a tree
        // dynamic 
    
        int length = 3;
        // generally: (cast *) malloc(length * size)
        // malloc returns void *, so we cast to int *
        int* arr = (int *)malloc(length * sizeof(int));
        // this allocates space for our array on the heap
        // could've just done: int arr[length], but this isn't dynamic
        
        // loop over array and fill with readInt
        int i;
        for(i = 0; i < length; i++) {
            printf("Enter array value %d: ", i);
            arr[i] = readInt();
            printf("\n");
        }

        // loop over again and print
        printf("[");
        for(i = 0; i < length; i++) {
            if (i < length - 1) {
                printf("%d, ", arr[i]);
                continue;
            }
            printf("%d" , arr[i]);
        }
        printf("]\n");

        // free malloc'd array pointer
        free(arr);
}
