/*
 * implementation for linked-list-based generic FIFO queue
 */
typedef struct qnode {
	struct qnode *next;
	void *element;
} QNode;

#include "ADTs/llistqueue.h"
#include <stdlib.h>
#include <stdbool.h>
/* any other includes needed for the implementation */

typedef struct q_data {
    /* flesh out the instance specific data structure */
	QNode *head;
	QNode *tail;
	long size;
	void (*freeValue)(void *v);
} QData;
/* any other data structures needed */

static void purge(QData *qd, void (*freeV)(void *e)) {
    if (freeV != NULL) {
        QNode *p;

        for (p = qd->head; p != NULL; p = p->next)
            (*freeV)(p->element);
    }
}

static void freeList(QData *qd) {
	QNode *q, *d = NULL;
	for (q = qd->head; q != NULL; q = d) {
		q = d->next;
		free(q);
	}
}
static void q_destroy(const Queue *q) {
    /* implementation of the destroy() method */
	QData *qd = (QData *)q->self;
    	purge(qd, qd->freeValue);
	freeList(qd);
	free(qd);
	free((void *)q);
}

static void q_clear(const Queue *q) {
    /* implementation of the clear() method */
	QData *qd = (QData *)q->self;
    	purge(qd, qd->freeValue);
	freeList(qd);
	qd->head = qd->tail = NULL;
	qd->size = 0L;
}

static bool q_enqueue(const Queue *q, void *element) {
    /* implementation of the enqueue() method */
    QData *qd = (QData *)q->self;
    QNode *new = (QNode *)malloc(sizeof(QNode));
    bool status = (new != NULL);
    if(status) {
		QNode *prev = qd->tail;
		new->next = NULL;
		new->element = element;

		if(prev == NULL) {
			qd->head = new;
			qd->tail = new;
	
		} else {
			prev->next = new;
			qd->tail = new;

		}
		qd->size++;
    }

    return status;
}

static bool q_front(const Queue *q, void **element) {
    /* implementation of the front() method */
    QData *qd = (QData *)q->self;
    bool status = (qd->size > 0L);
    if(status) {
	    *element = qd->head->element;
    }
    return status;
}

static bool q_dequeue(const Queue *q, void **element) {
    /* implementation of the dequeue() method */
    QData *qd = (QData *)q->self;
    bool status = (qd->size > 0L);
    if(status){
	    QNode *p = qd->head;
	    if((qd->head = p->next) == NULL){
		    qd->tail = NULL;
	    }
	    *element = p->element;
	    qd->size--;
	    free(p);
    }

    return status;

}

static long q_size(const Queue *q) {
    /* implementation of the size() method */
	QData *qd = (QData *)q->self;
	return qd->size;

}

static bool q_isEmpty(const Queue *q) {
    /* implementation of the isEmpty() method */
	QData *qd = (QData *)q->self;
	return (qd->size == 0L);
}

static void **genArray(QData *qd) {
    void **theArray = NULL;
	if(qd->size > 0L) {
		theArray = (void **)malloc(qd->size*sizeof(void *));
		if(theArray != NULL) {
			long i = 0L;
			QNode *g;
			for(g=qd->head; g != NULL; g = g->next) {
				theArray[i++] = g->element;
			}
		}
	}
	return theArray;
}

static void **q_toArray(const Queue *q, long *len) {
    /* implementation of the toArray() method */
	QData *qd = (QData *)q->self;
	void **tmp = genArray(qd);
	if (tmp != NULL) {
		*len = qd->size;
	}
	return tmp;
}

static const Iterator *q_itCreate(const Queue *q) {
    /* implementation of the itCreate() method */
	QData *qd = (QData *)q->self;
	const Iterator *it = NULL;
	void **tmp = genArray(qd);
	if(tmp != NULL) {
		it = Iterator_create(qd->size, tmp);
	}
	if(it == NULL) {
		free(tmp);
	}
	return it;
}

static const Queue *q_create(const Queue *q);
/* this is just declaring the signature for the create() method; it's
   implementation is provided below */

static Queue template = {
    NULL, q_create, q_destroy, q_clear, q_enqueue, q_front, q_dequeue, q_size,
    q_isEmpty, q_toArray, q_itCreate
};

static const Queue *newQueue(void (*freeV)(void*)) {
    Queue *q = (Queue *)malloc(sizeof(Queue));

    if (q != NULL) {
        QData *qd = (QData *)malloc(sizeof(QData));

        if (qd != NULL) {
            qd->size = 0L;
            qd->head = NULL;
            qd->tail = NULL;
            qd->freeValue = freeV;
            *q = template;
            q->self = qd;
        } else {
            free(q);
            q = NULL;
        }
    }
    return q;
}

static const Queue *q_create(const Queue *q) {
    /* implementation of the create() method */
	QData *qd = (QData *)q->self;
	return newQueue(qd->freeValue);

}

const Queue *LListQueue(void (*freeValue)(void *e)) {
    /* implementation of the structure-specific constructor */
	return newQueue(freeValue);
}

const Queue *Queue_create(void (*freeValue)(void *e)) {
    /* implementation of the generic constructor */
	return newQueue(freeValue);
}
