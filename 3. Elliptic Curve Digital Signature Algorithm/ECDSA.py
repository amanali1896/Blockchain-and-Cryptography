#the package used is PyCrytodom

from Crypto.Hash import SHA256 #for hashing
from Crypto.PublicKey import ECC #for eliptical curve cryptographic key creation
from Crypto.Signature import DSS #for signature creation and verification

'''
The key is generated on the secp256k1 elliptical curve using the ECC.generate method,
and both public and private keys are exported
'''
key = ECC.generate(curve='P-256') #generates a public private key pair


with open('ecc.pub', 'wt') as f:
    f.write(key.public_key().export_key(format='PEM')) #PEM is for privacy enhanced mail.
    #above is public key
'''
PEM (Privacy Enhanced Mail) was an IETF standard for securing emails 
via a Public Key Infrastructure. It is specified in RFC 1421-1424.
'''

with open('ecc.pem', 'wt') as f:
    f.write(key.export_key(format='PEM'))
#the corresponding private key

'''
Messages that need to be signed are hashed using the SHA256 algorithm, and then a signer
object is created using the DSS package by providing a private key. The hashed message is
then signed by the owner

'''

message = b'Message for signature'
key = ECC.import_key(open('ecc.pem').read()) #private
h = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3') #the new key is signed with fips-186-3 standard
'''
FIPS 186-3
Digital Signature Standard (DSS)
'''

signature = signer.sign(h) #signed with private key

'''
Signature verification in the following code is similar to that of signing. The received
message is hashed initially since the hashing was performed at the sender side as well. The
distributed public key is imported and used to create a new DSS object for verification. The
hashed message and the received signature are used for verification. The verify function
throws a ValueError if the message or signature was tampered with.
'''

h = SHA256.new(message)
key = ECC.import_key(open('ecc.pub').read()) #the public key which was initially generated
verifier = DSS.new(key, 'fips-186-3')
try:
    verifier.verify(h, signature)
    print("It is an authentic message.") #it will be authentic since the public key corresponds
    #with the private key. this was generated initially using ECC.generate.

except ValueError:
    print("It is not an authentic messaage.")
