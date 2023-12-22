#include <string>
#include <iostream>
#include <algorithm>
#include "ccipher.h"


// -------------------------------------------------------
// Caesar Cipher implementation


// -------------------------------------------------------

CCipher::CCipher():Cipher() {
}

CCipher::CCipher(int rot):Cipher() {
	if (rot < 0) {
		cout << "Error: Caesar cipher is less than 0\n" << endl;
		exit(1);
	}

	string albet = "abcdefghijklmnopqrstuvwxyz";
	rotate_string(albet, rot);
	this->smile->cipher_alpha = albet;
}

CCipher::~CCipher() {
				
}

//string CCipher::encrypt(string raw) {
	//return Cipher::encrypt(raw);
//}

//string CCipher::decrypt(string enc) {
	//return Cipher::decrypt(enc);
//}

// Rotates the input string in_str by rot positions
void rotate_string(string& in_str, int rot)
{
    string albet = "";
    for (unsigned int count = 0; count < in_str.length(); count++) {
    	albet += in_str[(count+rot)%in_str.length()];
    }
    in_str = albet;
}
