from Crypto.Hash import SHA512
from Crypto.PublicKey import RSA
import json

data = input()

key_pair = False
with open("private_key.pem", 'r') as myfile:
	key_pair = RSA.importKey(myfile.read())

encrypted_data = SHA512.new(data.encode()).digest()
signature = key_pair.sign(encrypted_data, "")
print(signature[0])
