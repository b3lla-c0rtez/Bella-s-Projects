#include <stdio.h>
#include <stdlib.h>
#define BLOCK_SIZE 2

struct Line {
    unsigned char data[BLOCK_SIZE]; // 2-byte blocks
    unsigned int tag; // Assume tag is at most 32 bits
    unsigned char valid; // valid bit
};

struct Cache {
    struct Line *lines;
    int numLines;
};

unsigned int getOffset(unsigned int address) {
    return address & 0x1; // 2-byte blocks, so 1 offset bit
}

unsigned int getSet(unsigned int address) {
    return (address >> 1) & 0x7; // 2-byte blocks; 8 sets so 3 set bits
}

unsigned int getTag(unsigned int address) {
    return address >> 4; // total of 4 bits for offset and set
}

struct Cache* mallocCache(int numLines) {
    struct Cache* obj = (struct Cache *)malloc(sizeof(struct Cache)); // malloc to cache
    obj->lines = (struct Line *)malloc(numLines * sizeof(struct Line)); // malloc to pointer
    obj->numLines = numLines; //access numlines
    
    for (int i =0; i < numLines; i++) {
        obj->lines[i].valid = 0; //struct line instance
    }
    
    return obj; // return cache 
}

void freeCache(struct Cache *cache) {
    free(cache->lines);
    free(cache);
}

void printLine(struct Line *line, unsigned int set) {
    unsigned char *data = line->data;
    printf("set: %x - tag: %x - valid: %u - data: %.2x %.2x\n",
    set, line->tag, line->valid, data[0], data[1]);
}

void printCache(struct Cache *cache) {
    for(int i = 0; i < cache->numLines; i++) {
        if(cache->lines[i].valid == 1) { // checking if lines are valid
            printLine(&cache->lines[i], i); // printing valid lines 
        }
    }
}

void readValue(struct Cache *cache, unsigned int address) {
    unsigned int s = getSet(address); // gets the set
    unsigned int t = getTag(address); // gets the tag 
    
    struct Line *line = &cache->lines[s]; // checking cache at a specified set address
    if(line->valid) { // checking if line if valid
        if(line->tag != t) { // if there is a tag mismatch
            printf("conflict miss \n");
        }
        printf("hit \n");
        printLine(line, s); // print line and set
    } else {
        printf("cold miss \n"); // if specified address is not found
    }
    
}

void writeValue(struct Cache *cache, unsigned int address, unsigned char *newData) {
    unsigned int s = getSet(address);
    unsigned int t = getTag(address);
    
    struct Line *line = &cache->lines[s];
    if (line->valid && line->tag != t) {
        unsigned char *data = line->data;
        printf("evicting line - ");
        printLine(line, s);
    }

    for (int i = 0; i < BLOCK_SIZE; ++i) {
        line->data[i] = newData[i];
    }
    
    line->tag = t;
    line->valid = 1;
    
    printf("wrote set: ");
    printLine(line, s);
}

unsigned int readUnsignedIntFromHex() {
    char buffer[10];
    char *p = NULL;
    unsigned int n;
    while (1) {
        fgets(buffer, sizeof(buffer), stdin);
        n = strtoul(buffer, &p, 16);
        if (buffer != p) {
            break;
        }
        printf("Invalid input - try again: ");
    }
    return n;
}

int main() {
    struct Cache *cache = mallocCache(8);
    char buffer[10];
    char c;
    do {
        printf("Enter 'r' for read, 'w' for write, 'p' to print, 'q' to quit: ");
        fgets(buffer, sizeof(buffer), stdin);
        c = buffer[0];
        if (c == 'r') {
            printf("Enter 32-bit unsigned hex address: ");
            unsigned int a = readUnsignedIntFromHex();
            readValue(cache, a);
        } else if (c == 'w') {
            printf("Enter 32-bit unsigned hex address: ");
            unsigned int a = readUnsignedIntFromHex();
            printf("Enter 32-bit unsigned hex value: ");
            unsigned int v = readUnsignedIntFromHex();
            unsigned char *data = (unsigned char *)&v;
            writeValue(cache, a, data);
        } else if (c == 'p') {
            printCache(cache);
        }
    } while (c != 'q');
    freeCache(cache);
}
