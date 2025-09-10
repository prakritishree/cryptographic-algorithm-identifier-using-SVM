import os
import csv
from Crypto.Cipher import AES, DES, RC5
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Step 1: Define the plaintext message
plaintext = b"Hello, World!"  # This is the message we will encrypt

# Step 2: Create a CSV file to store the ciphertexts
with open('ciphertext.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Algorithm', 'Ciphertext'])  # Write the header row

    # Step 3: AES Encryption
    key_aes = os.urandom(16)  # Generate a random 128-bit key
    iv_aes = os.urandom(16)   # Generate a random initialization vector
    cipher_aes = AES.new(key_aes, AES.MODE_CBC, iv_aes)
    padded_plaintext = pad(plaintext, AES.block_size)  # Pad plaintext
    ciphertext_aes = cipher_aes.encrypt(padded_plaintext)
    writer.writerow(['AES', ciphertext_aes.hex()])  # Write AES ciphertext

    # Step 4: DES Encryption
    key_des = os.urandom(8)  # Generate a random 64-bit key
    iv_des = os.urandom(8)   # Generate a random initialization vector
    cipher_des = DES.new(key_des, DES.MODE_CBC, iv_des)
    padded_plaintext = pad(plaintext, DES.block_size)  # Pad plaintext
    ciphertext_des = cipher_des.encrypt(padded_plaintext)
    writer.writerow(['DES', ciphertext_des.hex()])  # Write DES ciphertext

    # Step 5: RC5 Encryption
    key_rc5 = os.urandom(16)  # Generate a random 128-bit key for RC5
    cipher_rc5 = RC5.new(key_rc5, RC5.MODE_ECB)  # Create a new RC5 cipher in ECB mode
    padded_plaintext_rc5 = pad(plaintext, RC5.block_size)  # Pad plaintext
    ciphertext_rc5 = cipher_rc5.encrypt(padded_plaintext_rc5)
    writer.writerow(['RC5', ciphertext_rc5.hex()])  # Write RC5 ciphertext

    # Step 6: RSA Encryption
    private_key = RSA.generate(2048)  # Generate RSA key pair
    public_key = private_key.publickey()
    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext_rsa = cipher_rsa.encrypt(plaintext)
    writer.writerow(['RSA', ciphertext_rsa.hex()])  # Write RSA ciphertext

# Step 7: Print completion message
print("Ciphertexts generated and saved to 'ciphertext.csv'.")