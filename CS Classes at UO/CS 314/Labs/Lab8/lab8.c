#include <stdio.h>
#include <math.h>

// COMPILE WITH -lm !!!
void printTSO(int blockSizeInBytes, int numSets, int archSizeInBits) {
        int setBits = 0;
        if (numSets > 1) {
                setBits = log2(numSets);
        }
        int offsetBits = log2(blockSizeInBytes);
        int tagBits = archSizeInBits - setBits - offsetBits;
        printf("%dB blocks, %d sets, %d-bit architecture: %d tag bits, %d set bits, %d offset bits.\n", blockSizeInBytes, numSets, archSizeInBits, tagBits, setBits, offsetBits);
}

// LAB 8: 256B block, 1 set, 32 bit arch
//what is a cache?
// fast seection of memory close to the CPU
// fast beecause hardware, more expensive than RAM 
//
// split into blocks 
// cache blocks implicitly divide RAM into blocks of the same size 
// block is how much you read into cache at a time

// e.g. for a cache with block size 8 bytes, RAM gets split up into 8 byte sections 

//256 blocks, 1 set, 32-bit architecture; 24 tag bits, 0 set bits, 8 offset bits
// what this means:
// for some address, e.g. 0x12345678 
//format is <tag><set><offset>, so bytes 3-1 are tag and byte 0 is offset 
//we grab bytes 0x12345600 through 0x123456FF into cache
// implicit split into 256B sections
//0x12345600 through 0x123456FF all grab the same block from RAM 
// roughly, depending on alignment
// then we read from cache w/offset, like a pointer into cache

//block size of 2 bytes
//splits RAM into pairs of bytes, one pair read to cache at a time 
//e.g. 0x12345678 would read 0x12345678 and 0x12345679 into cache
// access cache by 0 or 1 (LSB of 8 or 9) 

// LAB 8: 256B block, 1 set, 32 bit arch 
// <tag><set><offset>

unsigned int getOffset(unsigned int address) {
        unsigned int mask = 0x000000FF;
        unsigned int offset = address & mask;
        return offset;
}
unsigned int getTag(unsigned int address) {
        unsigned int mask = 0xFFFFFF00;
        unsigned int tag = address & mask;
        tag >>= 8;
        return tag;
}
void main() {
        printTSO(256, 1, 32);
        unsigned int testAddr1 = 0x12345678;
        unsigned int testAddr2 = 0x87654321;
        // uncomment after implementing
        printf("0x%08x: offset - %x, tag - %x.\n", testAddr1, getOffset(testAddr1), getTag(testAddr1));
        printf("0x%08x: offset - %x, tag - %x.\n", testAddr2, getOffset(testAddr2), getTag(testAddr2));
}