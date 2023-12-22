#include <string>
#include <iostream>
#include <vector>
#include "kcipher.h"




/* Helper function definitions
 */
bool is_valid(string alpha);
// -------------------------------------------------------
// Running Key Cipher implementation
// -------------------------------------------------------

struct KCipher::RKCipherCheshire {
	vector<string> k;
	int p;
};


KCipher::KCipher() : Cipher() {
	ksmile = new struct RKCipherCheshire;
	string fill (MAX_LENGTH, 'a');
	add_key(fill);
	set_id(0);
}

KCipher::KCipher(string alpha) : Cipher() {
	ksmile = new struct RKCipherCheshire;
	add_key(alpha);
}

KCipher::~KCipher() {
	delete ksmile;
}

void KCipher::add_key(string alpha) {
	if (alpha.empty() || !(is_valid(alpha))) {
		cerr << "Invalid running key: " << alpha << endl;
		exit(EXIT_FAILURE);
	}
	else {
		ksmile->k.push_back(alpha);
	}
}

void KCipher::set_id(unsigned int bp) {
	if (bp <= ksmile->k.size()) {
		ksmile->p = bp;
	}
	else {
		cerr << "Warning: invalid id: " << bp << endl;
		exit(EXIT_FAILURE);
	}
}

string KCipher::encrypt(string raw) {
	cout << "Encrypting...";
	string retStr;
	string b = ksmile->k[ksmile->p];
	size_t b_len = b.length();
	string key_new;

	for (unsigned int i = 0; i<b_len; i++) {
		char l = b.at(i);
		if (l != ' ') {
			key_new += b[i];
		}
	}

	for (unsigned int i=0; i<raw.length(); i++) {
		char l = raw.at(i);
		if (l == ' ') {
			key_new.insert(i, 1, l);
		}
	}

	for (size_t i=0; i<raw.length(); i++) {
		string albet = this->smile->cipher_alpha;
		char l = raw.at(i);
		if (l != ' ') {
			if (islower(l)) {
				rotate_string(albet, (key_new[i] - 'a'));
				retStr += albet[l - 'a'];
			} else {
				rotate_string(albet, (key_new[i] - 'a'));
				retStr += albet[l - 'A']-32;
			}
		} else {
			retStr += ' ';
		}
	}
	cout << "Done" << endl;
	return retStr;
}

string KCipher::decrypt(string enc) {
	cout << "Decrypting...";
	string retStr;
	string b = ksmile->k[ksmile->p];
	string key_new;

	for (unsigned int i = 0; i<b.size(); i++) {
		char l = b.at(i);
		if (l != ' ') {
			key_new += b[i];
		}
	}

	for (unsigned int i=0; i<enc.length(); i++) {
		char l = enc.at(i);
		if (l == ' ') {
			key_new.insert(i, 1, l);
		}
	}

	for (unsigned int i=0; i<enc.length(); i++) {
		string albet = this->smile->cipher_alpha;
		char l = enc.at(i);
		if (l != ' ') {
			if (islower(l)) {
				rotate_string(albet, key_new[i] - 'a');
				retStr += this->smile->cipher_alpha[albet.find(l)];
			}
			if (isupper(l)) {
				rotate_string(albet, key_new[i] -'a');
				retStr += (this->smile->cipher_alpha[albet.find(l+32)]-32);
			}
		} else {
			retStr += ' ';
		}
	}

	cout << "Done" << endl;
	return retStr;
}

bool is_valid(string alpha) {
	for (long unsigned int i = 0; i<alpha.length(); i++) {
		char l = alpha.at(i);
		if (l >= 65 && l <= 90) {
			return false;
		} else if (l == ' ') {
			continue; 
		}
	}
	return true;
}
