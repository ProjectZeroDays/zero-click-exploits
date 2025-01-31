#ifndef SECURE_CRYPTO_H
#define SECURE_CRYPTO_H

#include <stddef.h>

void secure_crypto_init();
void secure_crypto_cleanup();

int secure_crypto_encrypt(const unsigned char* data, size_t data_len, unsigned char* encrypted_data, size_t* encrypted_data_len);
int secure_crypto_decrypt(const unsigned char* encrypted_data, size_t encrypted_data_len, unsigned char* data, size_t* data_len);

#endif
