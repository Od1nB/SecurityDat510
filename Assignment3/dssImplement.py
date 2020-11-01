import hashlib




#To do


#Building blocks of Digital Signature Scheme
#Key exchange protocol for public and private keys
#A hash function
#A per user public key
#A per user private key 
message = "Do you want to 3ncrypt some strings? Alice"

"Both agree on public generator and a prime"
q = 10009
a = 337 #The generator has to be a primitive root of the prime q

print(f"Big prime: {q} and generator which is primitive root of q: {a}")

"Both choose a private key themselves and use this to generate a public key"

privAlice = 43
publicAlice = pow(a,privAlice,q)
privBob = 69 
publicBob = pow(a,privBob,q)

print(f"Alice chooses a private key, {privAlice} and generates a public key from this {publicAlice}")
print(f"Bob chooses a private key, {privBob} and generates a public key from this {publicBob}")

"Alice wants to send a message to Bob. She then makes a signature to send with the message."

"Alice starts with hashing her message"
hashedMessage = hashlib.sha256(message.encode())
print(f"Alice uses a cryptograpic hash on her message to transform #{message}# to {hashedMessage.hexdigest()}")




