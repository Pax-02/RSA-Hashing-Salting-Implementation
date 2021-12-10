# Import hashlib library
import hashlib

# Message to be salted
message=(input("What message do you want to salt?: "))
# adding the value to the given message
salt_message="Strongpswd-"+message
# hash the salt message with sha512
hash=hashlib.sha512(salt_message.encode())
# hash the message not salted with sha512
hash_message=hashlib.sha512(message.encode())
# print the result of salting
print("The message salted is: "+str(salt_message)+ " it's hash is: "+hash.hexdigest())
# print the hash of the message not salted
print("The message not salted is: "+str(message)+ " it's hash is: "+hash_message.hexdigest())