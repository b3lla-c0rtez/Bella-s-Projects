#include <stdio.h>
#define UI unsigned int

unsigned char getByte(UI x, int i) {
    //convert i from bytes to bits
    // i = 0, 1, 2, or 3 and we want 0, 8, 16, 24
    UI shift = i << 3;
    // create a mask and shift it into position
    //remember: 0xFF is 1111 1111
    UI mask = 0xFF << shift; // 0xFF is 0x000000FF, shift of 8: 0x0000FF00, shift of 16: 0x00FF0000, of 24: 0xFF000000
    //get the bytes from x and shift it into the lowest byte
    UI result = mask & x; // e.g. if x was 0xABCDEF12 and mask was 0x00FF0000, result is 0x00CD0000
    // 0xABCDEF12
    // 0x00FF0000
    // 0x00CD0000
    return (mask & x) >> shift; // e.g. 0x00CD0000 --> 0x000000CD
}

UI swap(UI x, int a, int b) {

    UI aVal = getByte(x, a); // isolate byte a of x
    UI bVal = getByte(x, b); // isolate byte b of x
    UI aShift = a << 3; // multiply by 8
    UI bShift = b << 3; // multiply by 8
    UI aMask = 0xFF << aShift; // shift 0xFF left by 8*a
    UI bMask = 0xFF << bShift; // shift 0xFF left by 8*b
    x &= ~aMask; // invert mask (e.g., 0x000000FF -> 0xFFFFFF00) to clear space for the bVal
    x &= ~bMask; // invert mask (e.g., 0x000000FF -> 0xFFFFFF00) to clear space for the aVal
    x |= bVal << aShift; // align bVal, combine with x
    x |= aVal << bShift; // align aVal, combine with x
    return x;
}

int main() {
    UI test = 0xABCDEF12;
    for (int i = 0; i < 3; i++) {
        printf("swap(0x%08X, 3, %d): 0x%08X.\n", 
        test, i, swap(test, 3, i));
    }
}
