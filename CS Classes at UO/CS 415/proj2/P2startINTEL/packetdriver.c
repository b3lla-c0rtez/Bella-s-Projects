#include <pthread.h>
#include <stdio.h>
#include "freepacketdescriptorstore__full.h"
#include "freepacketdescriptorstore.h"
#include "networkdevice__full.h"
#include "pid.h"
#include "networkdevice.h"
#include "packetdriver.h"
#include "packetdescriptor.h"
#include "packetdescriptorcreator.h"
#include "BoundedBuffer.h"
#include "queue.h"
#include "diagnostics.h"
#include "destination.h"
#include "fakeapplications.h"

static BoundedBuffer *bb_send = NULL;
static BoundedBuffer *bb_rec[MAX_PID+1];
static PacketDescriptor *pd_send = NULL;
static PacketDescriptor *pd_rec = NULL;
static NetworkDevice *nd_pointer;
static unsigned long bb_size;
static FreePacketDescriptorStore *fpds_pointer;

static void *send_func() {
    // grab buffer
    // send to network device
    // deposit to fpds
    // printf("where are my brain cells\n");
    while (1) {
        if ((bb_send->nonblockingRead(bb_send, (void **)&pd_send)) == 0) {
            bb_send->blockingRead(bb_send, (void **)&pd_send); // can be better with nonblocking, checking if it's equal to 0
        }
        nd_pointer->sendPacket(nd_pointer, pd_send); // optional: try to resend if unsuccesful 
        if ((fpds_pointer->nonblockingPut(fpds_pointer, pd_send)) == 0) {
            fpds_pointer->blockingPut(fpds_pointer, pd_send);
        }
    }
    return NULL; 
}

static void *rec_func() {
    // take from fpds
    // initialize pd
    // register with network device
    // await incoming package
    // find pid
    // put in receiver buffer
    // printf("i feel like i am going insane\n");
    while (1) {
        if ((fpds_pointer->nonblockingGet(fpds_pointer, &pd_rec)) == 0) {
            fpds_pointer->blockingGet(fpds_pointer, &pd_rec); // can be better
        }
        initPD(pd_rec);
        nd_pointer->registerPD(nd_pointer, pd_rec);
        nd_pointer->awaitIncomingPacket(nd_pointer);
        PID pid = getPID(pd_rec);
        if ((bb_rec[pid]->nonblockingWrite(bb_rec[pid], pd_rec)) == 0) {
            bb_rec[pid]->blockingWrite(bb_rec[pid], pd_rec); // can be better
        }
    }
    return NULL;
}

/*any global variables required for use by your threads and your driver routines */
/* definition[s] of function[s] required for your thread[s] */
void init_packet_driver(NetworkDevice *nd, void *mem_start, unsigned long mem_length, FreePacketDescriptorStore **fpds_ptr) {
/* create Free Packet Descriptor Store using mem_start and mem_length */
    fpds_pointer = FreePacketDescriptorStore_create(mem_start, mem_length);
    nd_pointer = nd;

/* create any buffers required by your thread[s] */
    bb_size = fpds_pointer->size(fpds_pointer);
    bb_send = BoundedBuffer_create(MAX_PID+1); 

    for (int i; i<MAX_PID+1; i++) {
        bb_rec[i] = BoundedBuffer_create(bb_size/(MAX_PID+1)); // loop through and allocate
    }

/* create any threads you require for your implementation */
    pthread_t sending; 
    pthread_t receiving;
    pthread_create(&sending, NULL, send_func, NULL);
    pthread_create(&receiving, NULL, rec_func, NULL);

/* return the FPDS to the code that called you */
    *fpds_ptr = fpds_pointer;
}

void blocking_send_packet(PacketDescriptor *pd) {
/* queue up packet descriptor for sending */
/* do not return until it has been successfully queued */
    bb_send->blockingWrite(bb_send, (void *)pd);
}

int nonblocking_send_packet(PacketDescriptor *pd) {
/* if you are able to queue up packet descriptor immediately, do so and return 1 */
/* otherwise, return 0 */
    return bb_send->nonblockingWrite(bb_send, (void *)pd);
}

void blocking_get_packet(PacketDescriptor **pd, PID pid) {
/* wait until there is a packet for `pid’ */
/* return that packet descriptor to the calling application */
    bb_rec[pid]->blockingRead(bb_rec[pid], (void **)pd);
}

int nonblocking_get_packet(PacketDescriptor **pd, PID pid) {
/* if there is currently a waiting packet for `pid’, return that packet */
/* to the calling application and return 1 for the value of the function */
/* otherwise, return 0 for the value of the function */
    return bb_rec[pid]->nonblockingRead(bb_rec[pid], (void **)pd);
}
