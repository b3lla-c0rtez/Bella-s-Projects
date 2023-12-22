#include <string>
#include <iostream>
#include <vector>
#include "kcipher.h"
#include "vcipher.h"


// -------------------------------------------------------
// Running Key Cipher implementation
// -------------------------------------------------------
struct KCipher::RKCipherCheshire {
	vector <string> k;
	int p;	
};

VCipher::VCipher() : KCipher() {
}

VCipher::VCipher(string alpha) : KCipher() {
	ksmile = new KCipher::RKCipherCheshire;
	string new_string = "";
	while (new_string.length() < MAX_LENGTH) {
		new_string += alpha;
	}
	this->ksmile->k.push_back(new_string);
}


VCipher::~VCipher() {
}



