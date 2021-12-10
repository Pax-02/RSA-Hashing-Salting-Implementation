#Function to find the L.C.M. of two input number

def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
# inverse of the module function
def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1
# Message to be crpted:
m=input("what message do you want to encrypt: ")
# Two prime numbers p and q

p=73
q=79

# product of the two prime numbers

n=p*q
print("The product of prime numbers is "+str(n))
# Carmichael’s totient function of n is c: Computing lowest common multiple of (p-1) and (q-1)

c=compute_lcm((p-1),(q-1))

print ("The lcm is: "+str(c))

#any number between 1,c will be e
e=11
# Cryptinh the message: message power e modulus p*q
crypt=(int(m)**e)%n

print ("The encrypted message is: "+str(crypt))

# Generating Private key: privatekey=inverse of modulus(e and lcm(p-1,q-1)
private_key=modInverse(e,c)

print ("The private key is: "+str(private_key))

# Decrepted message= Crypted message power private_key modulus the product of prime numbers
decrypted_message=(crypt**private_key)%n

print ("The Decrypted message is: "+str(decrypted_message))