#include "cipher.h"

/* Cheshire smile implementation.
   It only contains the cipher alphabet
 */
struct Cipher::CipherCheshire {
    string cipher_alpha;
};

/* This function checks the cipher alphabet
   to make sure it's valid
 */
bool is_valid_alpha(string alpha);


// -------------------------------------------------------
// Cipher implementation
/* Default constructor
   This will actually not encrypt the input text
   because it's using the unscrambled alphabet
 */
Cipher::Cipher()
{
	smile = new CipherCheshire;
	this->smile->cipher_alpha = "abcdefghijklmnopqrstuvwxyz";
}

/* This constructor initiates the object with a
   input cipher key
 */
Cipher::Cipher(string cipher_alpha)
{
	smile = new CipherCheshire;
	this->smile->cipher_alpha = cipher_alpha;
}

/* Destructor
 */
Cipher::~Cipher()
{
	delete smile;
    
}


/* This member function encrypts the input text 
   using the intialized cipher key
 */
string Cipher::encrypt(string raw)
{
    cout << "Encrypting...";
    string retStr;
    string albet = "abcdefghijklmnopqrstuvwxyz";
    
	
    for (unsigned int count = 0; count < raw.length(); count++) {
	   unsigned int pos = find_pos(albet, LOWER_CASE(raw[count])); 

	   if (raw[count] == ' ') {
		   retStr += raw[count];
	   }

	   else if (raw[count] == UPPER_CASE(raw[count])) {
		   retStr += UPPER_CASE(this->smile->cipher_alpha[pos]);
	   }

	   else if (raw[count] == LOWER_CASE(raw[count])) {
		   retStr += LOWER_CASE(this->smile->cipher_alpha[pos]);
	   }

	   else {
	   	retStr += this->smile->cipher_alpha[pos];
	   }

    } 
	
	
    cout << "Done" << endl;

    return retStr;
}


/* This member function decrypts the input text 
   using the intialized cipher key
 */
string Cipher::decrypt(string enc)
{
    string retStr;
    cout << "Decrypting...";
    string albet = "abcdefghijklmnopqrstuvwxyz";
    
    for (unsigned int count = 0; count < enc.length(); count++) {
    	unsigned int pos = find_pos(smile->cipher_alpha, LOWER_CASE(enc[count]));

	if (enc[count] == ' ') {
		retStr += enc[count];
	}

	else if (enc[count] == UPPER_CASE(this->smile->cipher_alpha[pos])) {
		retStr += UPPER_CASE(albet[pos]);
	}

	else if (enc[count] == LOWER_CASE(this->smile->cipher_alpha[pos])) {
		retStr += LOWER_CASE(albet[pos]);
	}

	else {
		retStr += albet[pos];
	}
	
    }

    cout << "Done" << endl;

    return retStr;

}
// -------------------------------------------------------


//  Helper functions 
/* Find the character c's position in the cipher alphabet/key
 */
unsigned int find_pos(string alpha, char c)
{
    unsigned int pos = 0;
    
    bool fp = false;

    for (size_t f = 0; f < alpha.length(); f++) {
    	if(!fp) {
		if (alpha[f] == ' ') {
			continue;
		}

		if (alpha[f] == c) {
			fp = true;
			pos = f;
		}
	}
    }

    return pos;
}

/* Make sure the cipher alphabet is valid - 
   a) it must contain every letter in the alphabet 
   b) it must contain only one of each letter 
   c) it must be all lower case letters 
   ALL of the above conditions must be met for the text to be a valid
   cipher alphabet.
 */
bool is_valid_alpha(string alpha)
{
    bool is_valid = true;
    if(alpha.size() != ALPHABET_SIZE) {
        is_valid = false; 
    } else {
        unsigned int letter_exists[ALPHABET_SIZE];
        for(unsigned int i = 0; i < ALPHABET_SIZE; i++) {
            letter_exists[i] = 0;
        }
        for(unsigned int i = 0; i < alpha.size(); i++) {
            char c = alpha[i];
            if(!((c >= 'a') && (c <= 'z'))) {
                is_valid = false;
            } else {
                letter_exists[(c - 'a')]++;
            }
        }
        for(unsigned int i = 0; i < ALPHABET_SIZE; i++) {
            if(letter_exists[i] != 1) {
                is_valid = false;
            }
        }
    }

    return is_valid;
}
