#include "strheap.h"
#include "table.h"
#include "row.h"
#include <stdlib.h>
#include <string.h>
#include "ADTs/hashcskmap.h"

const CSKMap *m = HashCSKMap(0, 5.0, free_func);


typedef struct hash {
	// variables in here
	char *chrpnt;
	int count;
} Hash;


Hash *init_hash(char *nstrings) {
	Hash *hashpntr = (Hash *)malloc(sizeof(Hash));
	newhash->chrpnt = strdup(nstrings);
	newhash->count = 1;
	return hashpntr;
}

char *str_malloc(char *nstrings2) {
	Hash *newhash;

	//if in hashmap 
	if (m->get(m, nstrings2, &newhash)) {
		newhash->count += 1;
		return newhash->chrpnt;
	//if not in hashmap
	} else {
		newhash = init_hash(nstrings2);
		m->put(m, nstrings2, newhash);
	}

	return newhash->chrpnt;
}

bool str_free(char *nstrings3) {
	Hash *newhash;
	if (m->get(m, nstrings3, &newhash)) {
		newhash->count -= 1; 
		if (newhash->count == 0) {
			m->remove(m, nstrings3);
		}
		return true;
	} else {
		return false;
	}
}

void free_func(newhash) {
	free(newhash->chrpnt);
	free(newhash);
}