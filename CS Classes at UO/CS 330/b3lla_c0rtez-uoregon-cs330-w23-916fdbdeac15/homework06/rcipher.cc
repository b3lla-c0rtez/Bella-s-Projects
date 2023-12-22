#include <string>
#include <iostream>
#include "rcipher.h"

// -------------------------------------------------------
// ROT13 Cipher implementation
// -------------------------------------------------------
//

RCipher::RCipher() {
	//smile = new CipherCheshire();
	this->smile->cipher_alpha = "abcdefghijklmnopqrstuvwxyz";
	rotate_string(this->smile->cipher_alpha, 13);
}


RCipher::~RCipher(){
	
}
