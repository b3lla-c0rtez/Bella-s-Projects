#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

struct IntArray {
	int length;
	int *dataPtr;
};

struct IntArray* mallocIntArray(int length) {
    struct IntArray* result  = (struct IntArray*)malloc(sizeof(struct IntArray)); // take memory allocation of size of struct
    result -> dataPtr = (int *)malloc(length * sizeof(int)); // grab int of data pointer in struct result
    result -> length = length; // grab int of length in struct result
    return result; // return the result
}

void freeIntArray(struct IntArray *arrayPtr){
	free(arrayPtr); // free the array pointer
	free(arrayPtr->dataPtr); // free thei instance of the array pointer
}

void readIntArray(struct IntArray *array) {
	int i; 
    	char lineBuf[BUFSIZ];

	char *p = NULL;

	for(i=0; i<array->length;i++) { // sets i to 0, then loops through til length of array
		printf("Enter int: "); // has player enter int
		fgets(lineBuf, sizeof(BUFSIZ), stdin); // takes value
		long int n = strtol(lineBuf, &p, 10); // reads it
		if (p == NULL | n <= 0) { // if it is less than or equal to 0 or if it is null then it is not valid
			printf("Invalid input\n Enter length "); // if it is invalid
		} else {
			array->dataPtr[i] = n; /// if it is valid
		}
	}	
}

void swap(int *xp, int *yp) {
	int t0 = *xp; //sets temp 1
	int t1 = *yp; // sets temp 2
	*xp = t1; //switches value of temp 1
	*yp = t0; //switches value of temp 2
}

void sortIntArray(struct IntArray *array) {
	bool sorted = false;//sets bool to false
	int lastUnsort = array->length -1; //sets array equal to the array length minus 1
	while (!sorted) { // while something it is not sorted
		sorted = true; // set sorted to true
		for(int i=0; i< lastUnsort; i++) { // set i to 0, loops till length of array - 1
			for(int j=0; j<lastUnsort-i; j++) { // set j to 0, loops til array - 1 - i
				if ((array->dataPtr[j]) > (array->dataPtr[j+1])){ // if pointer value is greater than pointer value -1
					swap(&array->dataPtr[j], &array->dataPtr[j+1]);//swaps memory allocation
					sorted = false; //sorted is not true
				}
			}
		}
		lastUnsort -= 1; // array->length-1 -1
	}
}

void printIntArray(struct IntArray *array){
	//prints array
	printf("[ ");
	int i;
	for(i=0; i<array->length-1; i++) {
		printf("%d, ", array->dataPtr[i]); //array -> dataPtr[i] is the value at the location in the array
	}
	printf("%d ]\n", array->dataPtr[array->length-1]); // so there is no comma at the end of the code (uses array->dataPtr[array->length-1])
}

int main() {
	int size;
	char lineBuf[BUFSIZ];
	char *pt = NULL;
	long r;

	while(1){
		printf("Enter length: "); // takes length of array 
		fgets(lineBuf,sizeof(BUFSIZ),stdin); // takes that input
		r  = strtol(lineBuf, &pt, 10); // uses it
		if(r <= 0) { // if size is less than or equal to 0
			printf("Invalid input \n"); // it is an invalid input
			continue; 
		} else {
			break;
		}
	}
	size = r;
	struct IntArray *coolArray = mallocIntArray(size);
	readIntArray(coolArray);
	sortIntArray(coolArray);
	printIntArray(coolArray);
	freeIntArray(coolArray);
}
