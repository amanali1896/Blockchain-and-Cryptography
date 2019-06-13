#the package used is PyCrytodom

from Crypto.Cipher import AES # AES is used from the cipher package
from Crypto.Random import get_random_bytes # this is to generate a random key

with open("aes.key","wb") as file_out: #wb means writing in binary mode.
    #we open a file. and write the key to the file. this creates the ciphertext with
    #randomly selected key.
    key = get_random_bytes(16) #16 byte key
    file_out.write(key)

data = "plaintext"
cipher = AES.new(key, AES.MODE_EAX) #we create the cipher in EAX mode(encrypt then authenticate
#then translate #aes.new is aes object creation
cipher_text, tag = cipher.encrypt_and_digest(data.encode()) # generate cipher text and tag by
#encoding data.
with open("encrypted.bin", "wb") as file_out:
    [file_out.write(x) for x in (cipher.nonce, tag, cipher_text)]
print("Data is now encrypted")

# now the decryption process starts. The same files are now read. 

with open("aes.key","rb") as file_in: #rb means read in binary
    key = file_in.read(16) #same size key
with open("encrypted.bin","rb") as file_in:
    nonce, tag, cipher_text = [file_in.read(x) for x in (16, 16, -1)] #nonce, tag and ciphertext
    # is read

cipher = AES.new(key, AES.MODE_EAX, nonce) #aes object is created with same key and nonce.
data = cipher.decrypt_and_verify(cipher_text, tag) # this method perfoms verification. tag is
#provided to check for any modifications, if it exists. and cannot be omitted.

print("Decrypted data is : \"{}\"".format(data.decode()))



