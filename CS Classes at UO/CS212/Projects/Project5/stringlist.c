#include "stringlist.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define DEFAULT_CAPCAITY 50L

typedef struct self {
	long capacity;
	long size;
	char **array;
} Self;

static void lst_destroy(const StringList *lst){
	Self *self = (Self *) lst->self;
	long i;
	for (i=0; i<self->size; i++) {
		free(self->array[i]);
	}
	free(self->array);
	free(self);
	free((void *)lst);
}

static bool lst_append(const StringList *lst, char *st) {
	Self *self = (Self *) lst->self;

	bool ifSpace = (self->size < self->capacity);
	if(!ifSpace) {
		size_t nbytes = 2 * self -> capacity *sizeof(char *);
		char **temp = (char**)realloc(self->array, nbytes);
		if(temp != NULL){
			self->array = temp;
			self->capacity *= 2;
			ifSpace=true;
		}
	}
	if(ifSpace){ self->array[self->size++] = st; }
	return ifSpace;
}

static bool lst_get(const StringList *lst, long index, char **element){
	Self *self = (Self *)(lst->self);
	bool status = (index >= 0L && index < self->size);

	if(status) {
		*element = self->array[index];
	}

	return status;
	
}

static long lst_size(const StringList *lst) {
	Self *self = (Self *)(lst->self);
	return self->size;
}


const StringList *StringList_create(long capacity){
	StringList *lst = (StringList *)malloc(sizeof(StringList));
	if(lst != NULL) {
		Self *self = (Self*)malloc(sizeof(Self));
	if(self != NULL) {
		long cap = (capacity <= 0L) ? DEFAULT_CAPACITY : capacity;
		char **array = (char **)malloc(cap *sizeof(char*));
		if(array != NULL) {
			self->capacity = cap;
			self->size = 0L;
			self->array = array;

			lst->self = self;
			lst->destroy = lst_destroy;
			lst->append = lst_append;
			lst->size = lst_size;
			lst->get = lst_get;

			} else { free(self); free(lst); lst = NULL; }

		} else { free(lst); lst = NULL; }
	}
	return lst;
}




