#include "numlist.h"
#include <omp.h>

// Partitioning functions
// Serial partition
unsigned int NumList::partition(vector<int>& keys, unsigned int low, 
                                unsigned int high)
{
    // Use the last element as the pivot
    int pivot = keys[high];
   
    // TODO: Implement the serial partitioning method
    unsigned int i = low-1;
    
    for (unsigned int j = low; j < high; j++) {
    	if (keys[j] <= pivot) {
		i++;
		swap(keys[i], keys[j]);
	}
    }
    swap(keys[i+1], keys[high]);
    return i+1;
}


// Parallel partition
unsigned int NumList:: partition_par(vector<int>& keys, unsigned int low,
                                     unsigned int high)
{
    // Use the last element as the pivot
    int pivot = keys[high];


    // TODO: Implement the parallel partitioning method
    // There should be two #pragmas to parallelize the loop
    // First loop is calculating the lt and gt arrays
    // Second is when the integers are copied to the correct position (i.e.,
    // left or right side of the pivot
    int n = high - low + 1;

    if (n == 1) {
    	return low;
    }
    
    vector<int> B(n,0);
    vector<int> lt(n,0);
    vector<int> gt(n,0);

    #pragma omp parallel for
    for (unsigned int i = 0; i<(n-1); i++) {
    	B[i] = keys[low+i];
	//cout << "this is lt size " << lt.size() << endl;
	//cout << "this is gt size " << gt.size() << endl;
	if (B[i] <= pivot) {
		lt[i] = 1;
	} else {
		gt[i] = 1;
	}
    }
    B[n-1] = keys[low+n-1];


    for (unsigned int i = 1; i<n; i++) {
	lt[i] += lt[i-1];
	gt[i] += gt[i-1];
    }

    int k;
    k = low + lt[n-1];

    keys[k] = pivot;

    #pragma omp parallel for
    for (unsigned int i = 0; i<(n-1); i++) {
    	if (B[i] <= pivot) {
		keys[low + lt[i] - 1] = B[i];
	} else if (B[i] > pivot) {
		keys[k+gt[i]] = B[i];
	}
    }
    return k;

}

// Actual qsort that recursively calls itself with particular partitioning
// strategy to sort the list
void NumList::qsort(vector<int>& keys, int low, int high, ImplType opt)
{
    if(low < high) {
        unsigned int pi;
        if(opt == serial) {
            pi = partition(keys, low, high);
        } else {
            pi = partition_par(keys, low, high);
        }
        qsort(keys, low, pi - 1, opt);
        qsort(keys, pi + 1, high, opt);
    }
}

// wrapper for calling qsort
void NumList::my_qsort(ImplType opt)
{
    /* Initiate the quick sort from this function */
    qsort(list, 0, list.size() - 1, opt);
}
// Default constructor
// This should "create" an empty list
NumList::NumList() {
    /* do nothing */
    /* you will have an empty vector */
}
// Contructor
// Pass in a vector and the partitioning strategy to use
NumList::NumList(vector<int> in, ImplType opt) {
    list = in;
    my_qsort(opt);
}
// Destructor
NumList::~NumList() {
    /* do nothing */
    /* vector will be cleaned up automatically by its destructor */
}
// Get the element at index
int NumList::get_elem(unsigned int index)
{
    return list[index];
}
// Print the list
void NumList::print(ostream& os)
{
    for(unsigned int i = 0; i < list.size(); i++) {
        os << i << ":\t" << list[i] << endl;
    }
}
