#include <stdio.h>
#include <math.h>

void printTSO(int blockSizeInBytes, int numSets, int archSizeInBits) {
        int setBits = 0;
        if (numSets > 1) {
                setBits = log2(numSets);
        }
        int offsetBits = log2(blockSizeInBytes);
        int tagBits = archSizeInBits - setBits - offsetBits;
        printf("%dB blocks, %d sets, %d-bit architecture: %d tag bits, %d set bits, %d offset bits.\n", blockSizeInBytes, numSets, archSizeInBits, tagBits, setBits, offsetBits);
}


unsigned int getOffset(unsigned int address) {
        unsigned int mask = 0x000000FF;
        unsigned int offset = address & mask;
        return offset;
}


unsigned int getTag(unsigned int address) {
        unsigned int mask = 0xFFFFF000; //0xFFFFF000 
        unsigned int tag = address & mask; // this gave me 12345000
        tag >>= 12; // shift right 12 to get rid of the three 0s at the end
        return tag;
}

unsigned int getSet(unsigned int address) {
        unsigned int mask = 0x00000F00; // 0x00000F00
        unsigned int set = address & mask; // gives 600 and 300
        set >>= 8; // shift right by 8 to get 6 and 3
        return set;
}

void main() {
        printTSO(256, 16, 32);
        unsigned int testAddr1 = 0x12345678;
        unsigned int testAddr2 = 0x87654321;
        // uncomment after implementing
        printf("0x%08x: offset - %x, tag - %x, set - %x\n", testAddr1, getOffset(testAddr1), getTag(testAddr1), getSet(testAddr1));
        printf("0x%08x: offset - %x, tag - %x, set - %x\n", testAddr2, getOffset(testAddr2), getTag(testAddr2), getSet(testAddr2));
}

