# Import hashlib library
import hashlib

# Message to hash
message=input("write: ")
# Hashing using Sha-512
hash_message=hashlib.sha512(message.encode())
# printing the message hash
print(hash_message.hexdigest())