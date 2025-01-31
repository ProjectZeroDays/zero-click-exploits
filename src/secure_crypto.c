#include "secure_crypto.h"

#include <openssl/aes.h>
#include <openssl/rand.h>

static AES_KEY aes_key;
static int key_size = 0;

void secure_crypto_init() {
    if (!key_size) {
        // Generate a random key for AES encryption
        unsigned char key[AES_BLOCK_SIZE];
        RAND_bytes(key, AES_BLOCK_SIZE);
        AES_set_encrypt_key(key, AES_BLOCK_SIZE * 8, &aes_key);
        key_size = AES_BLOCK_SIZE;
    }
}

void secure_crypto_cleanup() {
    // Clear the AES key in memory
    memset(&aes_key, 0, sizeof(AES_KEY));
    key_size = 0;
}

int secure_crypto_encrypt(const unsigned char* data, size_t data_len, unsigned char* encrypted_data, size_t* encrypted_data_len) {
    if (!key_size) {
        secure_crypto_init();
    }

    // Check if the encrypted_data buffer is large enough
    if (*encrypted_data_len < data_len + AES_BLOCK_SIZE) {
        *encrypted_data_len = data_len + AES_BLOCK_SIZE;
        return -1;
    }

    // Encrypt the data using AES
    AES_encrypt(data, encrypted_data, &aes_key);

    // Add padding to the encrypted data
    for (size_t i = data_len; i < *encrypted_data_len; ++i) {
        encrypted_data[i] = 0x00;
    }

    *encrypted_data_len = data_len + AES_BLOCK_SIZE;
    return 0;
}

int secure_crypto_decrypt(const unsigned char* encrypted_data, size_t encrypted_data_len, unsigned char* data, size_t* data_len) {
    if (!key_size) {
        secure_crypto_init();
    }

    // Check if the data buffer is large enough
    if (*data_len < encrypted_data_len - AES_BLOCK_SIZE) {
        *data_len = encrypted_data_len - AES_BLOCK_SIZE;
        return -1;
    }

    // Remove padding from the encrypted data
    for (size_t i = encrypted_data_len - AES_BLOCK_SIZE; i < encrypted_data_len; ++i) {
        if (encrypted_data[i]) {
            return -1;
        }
    }

    // Decrypt the data using AES
    AES_decrypt(encrypted_data, data, &aes_key);

    *data_len = encrypted_data_len - AES_BLOCK_SIZE;
    return 0;
}
