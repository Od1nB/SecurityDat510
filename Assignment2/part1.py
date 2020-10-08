from Tools import SDES as sdes
#from Tools import SDES as sdes

plainTxT = [1,1,1,1,1,1,1,1]


# Cyclic group G with generator g:G = <g> (public parameters)
# used for making a private and public key for both alice and bob
#Exchange public keys and make a key with this one
# Kab is seed for any CSPRNG to generate a key used in a symmetric algorithm
#Use the key to encrypt, send, decrypt and then decrypt

#g = 2 z = p = 2q + 1 

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

#DH key exchange

"STEP 1 "
"Alice and Bob agree on some global parameters for a cyclic group"

publicPrime = 953
publicG = 2

print("STEP 1")
print("Alice and Bob agree on the cyclic group with Z="+str(publicPrime)+" with the generator g= "+str(publicG))

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
#print("Alices common key after sharing and then combining with Bobs public: "+str(commonAlice))
print("Alices creates their common key when combinig her secret with Bobs public key and gets: "+str(commonAlice))

commonBob = createSecretCommonKey(Alicepublic,BobSecret)
#print("Bobs common key after sharing and then combining with Alices public: "+str(commonBob))
print("Bob creates their common key when combinig his secret with Alices public key and gets: "+str(commonBob))

"STEP 5"
"Concered about the safety of the key they do a CSPRNG with their key as SEED, taking use of BBS"

print("STEP 5")

def calcNext(seed,length):
    p = 11
    q = 23
    M = p*q
    if length ==1:
        return ((seed ** 2) % M)
    else:
        tempSeed = seed
        output = []
        for i in range(length):
            tempNumb = ((tempSeed ** 2) % M)
            output.append(tempNumb)
            tempSeed = tempNumb
        return output
alicesKeyK = calcNext(commonAlice,1)
bobsKeyK = calcNext(commonBob,1)

alicesKeyK = convertDeciToTenBit(alicesKeyK)
bobsKeyK = convertDeciToTenBit(bobsKeyK)


encrypted = sdes.sdesEncryption(plainTxT,alicesKeyK)
print("Alice encrypted her plaintext "+str(plainTxT)+" with SDES and her keyK to this "+str(encrypted))

decrypted = sdes.sdesDecryption(encrypted,bobsKeyK)
print("Bob tried to decrypt this "+str(encrypted)+" from also and got this "+str(decrypted))
#ToDo

#Import SDES from other tasks DONE
#Make DH key exchange to make new shared Kab DONE
#Use BlumBlumShub for psuedorand numb

