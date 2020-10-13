from Tools import SDES as sdes

plainTxT = "3ncryPt10n 1s fuN"

def convertDeciToTenBit(deci):
    bits = "{0:b}".format(deci)
    if len(bits)>10:
        return "The decimalnumber is to big"

    while(len(bits)<10):
        bits = bits + "0"
    bitsArray = []

    for i in range(len(bits)):
        bitsArray.append(int(bits[i]))

    return bitsArray

#DH key exchange simulation

"STEP 1 "
"Alice and Bob agree on some global parameters for a cyclic group"

publicPrime = 953
publicG = 2

print("STEP 1")
print("Alice and Bob agree on the cyclic group with Z="+str(publicPrime)+" with the generator g="+str(publicG))

"STEP 2"
"Both Alice and Bob has to agree on their on private key and make a public key"


def createPublicKey(secretInt):
    return ((publicG ** secretInt) % publicPrime)

AliceSecret = 11
BobSecret = 7
Alicepublic = createPublicKey(AliceSecret)
Bobpublic = createPublicKey(BobSecret)

print("STEP 2")
print("Alice chooses the private key "+str(AliceSecret)+" and uses this to generate the public key: "+str(Alicepublic))
print("Bob chooses the private key "+str(BobSecret)+" and uses this to generate the public key: "+str(Bobpublic))

"STEP 3"
"Alice and Bob share public keys"
print("STEP 3")
print("Alice shares her public key "+str(Alicepublic)+" with Bob, and Bob shares his public key "+str(Bobpublic)+" with Alice")

"STEP 4"
"Alice and Bob creates the shared Key Kab on their own"

def createSecretCommonKey(publicKey, secretInt):
    return ((publicKey ** secretInt) % publicPrime)

print("STEP 4")

commonAlice = createSecretCommonKey(Bobpublic,AliceSecret)
print("Alices creates their common key when combinig her secret with Bobs public key and gets: "+str(commonAlice))

commonBob = createSecretCommonKey(Alicepublic,BobSecret)
print("Bob creates their common key when combinig his secret with Alices public key and gets: "+str(commonBob))

"STEP 5"
"Concered about the safety of the key they do a CSPRNG with their key as SEED, taking use of BBS"

print("STEP 5")
print("Alice and Bob uses the Blum Blum Shub method to generate a strong pseudo-random number for key use")
alicesKeyK = sdes.BBSrand(commonAlice,10) #Function present in the Tools/SDES.py file as additional functionality for this assignment
bobsKeyK = sdes.BBSrand(commonBob,10)
print("Alices secret key after BBS with her shared k:"+alicesKeyK+" and Bobs equivalent:"+bobsKeyK)

"STEP 6"

print("STEP 6")
print("Alices uses SDES as an encryption method and encrypts her plaintext ")
alicesKeyK = sdes.stringToArr(alicesKeyK)
encrypted = sdes.encryptString(plainTxT,alicesKeyK)

print("Alice encrypted her plaintext: "+plainTxT+" with SDES and her secret key to this: ")
print(encrypted)
print("Then she sent the encrypted text over the internet to Bob")

"STEP 7"

print("STEP 7")
print("Bob recieves the encrypted text and tries to decrypt it with their secret key")

bobsKeyK = sdes.stringToArr(bobsKeyK)
decrypted = sdes.decryptString(encrypted,bobsKeyK)
print("The results from Bobs decryption looks like this: "+decrypted)


