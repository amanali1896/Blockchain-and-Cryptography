#package used is PyCryptoDome

from Crypto.PublicKey import RSA #importing RSA
from Crypto.Cipher import PKCS1_OAEP # this is a kind of cipher described in RFC8017


message = "plaintext"
key = RSA.generate(2048) #generating a 2048 bit RSA Key
public = key.publickey() #The public key is exported from this generated key and made public.

#key object should be kept secret.

cipher = PKCS1_OAEP.new(public) #cipher object is created from this public key.
cipher_text = cipher.encrypt(message.encode()) #encryption is performed on the message using
#cipher object.
print("The data is now encrypted")

'''
the decryption operation is performed in a similar way to the encryption operation, but the
private part of the key pair(that is why we have to keep the key secret)
is used instead of the public part. The ciphertext is given as input to the decrypt method, 
which decrypts it and gives back the decrypted message

'''

cipher = PKCS1_OAEP.new(key)

message = cipher.decrypt(cipher_text)

print("Decrypted data is : \"{}\"".format(message.decode()))