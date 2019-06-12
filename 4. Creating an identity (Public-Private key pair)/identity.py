import binascii

from ecdsa import SigningKey, VerifyingKey, SECP256k1, keys


class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_key_pair(self):
        sk = SigningKey.generate(curve=SECP256k1)

        self.private_key = binascii.b2a_hex(sk.to_string()).decode()
        self.public_key = binascii.b2a_hex(sk.get_verifying_key().to_string()).decode()


account = Wallet()

account.generate_key_pair()

print("public key is %s" %account.public_key) #128 character public key

print("public key is %s" %account.private_key) #64 character (256 bit) private key


