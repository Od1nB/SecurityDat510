import time as t

key = [1,0,1,0,0,0,0,0,1,0]
ctx1 = "010001110000000101000000110011011100101100000001011101000000000101101110010101110101011101101110010001110000000101000111101110100100111110001000010001110110111001001100101011111001011101101110011011101011101001001111101011110000100101001010100010000100111111001101100101110100111100110010000000010101011101101110100100000100111110101111010001111010111101110100011101000000000101001100000000010110111010111010100010000100011101101110010011001010111110010111000000011000100010010000"
ctx2 = "000000011010011100110010110001100110010010100111110101111010011110011100011101000111010010011100000000011010011100000001100110011010000111011010000000011001110011101111011111100010010010011100100111001001100110100001011111101010000010110011110110101010000111000110001001001010000100100011101001110111010010011100010000011010000101111110000000010111111011010111110101111010011111101111101001111001110010011001110110100000000110011100111011110111111000100100101001111101101001000001"




def lshift1(list1):
    tempList = list1.copy()
    for i in range(len(list1)):
        list1[i-1] = tempList[i]
    return list1

def funcF(inputBit,subkey):
    expPer = [inputBit[3],inputBit[0],inputBit[1],inputBit[2],inputBit[1],inputBit[2],inputBit[3],inputBit[0]]

    for i in range(len(expPer)) :
        tempNumber = expPer[i]
        expPer[i] = int(tempNumber)^int(subkey[i])
    
    S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    epL = expPer[:4]
    epR = expPer[4:]

    rowS0 = epL[0]*2 + epL[3]
    colS0 = epL[1]*2 + epL[2]
    binS0 = list(bin(S0[rowS0][colS0]).replace("0b",""))
    #print(binS0)
    if len(binS0) != 2:
        binS0.insert(0,0)

    rowS1 = epR[0]*2 + epR[3]
    colS1 = epR[1]*2 + epR[2]
    binS1 = list(bin(S1[rowS1][colS1]).replace("0b",""))

    if len(binS1) != 2:
        binS1.insert(0,0)
    
    P4 = [binS0[1],binS1[1],binS1[0],binS0[0]]
    return P4


def keygenerating(tenBitKey):
    permutedKey = [tenBitKey[2],tenBitKey[4],tenBitKey[1],tenBitKey[6],tenBitKey[3],tenBitKey[9],tenBitKey[0],tenBitKey[8],tenBitKey[7],tenBitKey[5]]
    circularL = permutedKey[:5]
    circularR = permutedKey[5:]

    lshiftKey = lshift1(circularL)+lshift1(circularR)
    subKey1 = [lshiftKey[5],lshiftKey[2],lshiftKey[6],lshiftKey[3],lshiftKey[7],lshiftKey[4],lshiftKey[9],lshiftKey[8]]

    lshiftKey2 = lshift1(lshift1(lshiftKey[:5])) + lshift1(lshift1(lshiftKey[5:]))
    subKey2 = [lshiftKey2[5],lshiftKey2[2],lshiftKey2[6],lshiftKey2[3],lshiftKey2[7],lshiftKey2[4],lshiftKey2[9],lshiftKey2[8]]

    return subKey1,subKey2


def ipfunc(arr, typ):
    temp = arr.copy()
    if(typ):
        arr = [temp[1],temp[5],temp[2],temp[0],temp[3],temp[7],temp[4],temp[6]]
    else:
        arr = [temp[3],temp[0],temp[2],temp[4],temp[6],temp[1],temp[7],temp[5]]
    return arr
#print("org string: "+str([1,0,0,0,0,0,1,1]))
#IP = ipfunc([1,0,0,0,0,0,1,1],True)
#print("ip function"+str(IP))
#print("The invers try: "+str(ipfunc(IP,False)))

def funcFk(inputBits, subkey):
    lbits = inputBits[:4]
    rbits = inputBits[4:]   

    bigF = funcF(rbits,subkey)
    outputLeft = []
    for i in range(len(bigF)):
        outputLeft.append(int(bigF[i])^int(lbits[i]))
    return outputLeft + rbits

def SW(bits):
    return bits[4:] + bits[:4]

plaintxt = [1,0,1,0,1,0,1,0]
#keygenerating(key)

def sdesEncryption(eightbitInput, tenbitkey):
    subKeys = keygenerating(tenbitkey) #keygen
    permBits = ipfunc(eightbitInput,True) #Initial per
    #print("initpermbits: "+str(permBits))

    fk1 = funcFk(permBits,subKeys[0])
    #print("after fk1 bits: "+str(fk1))
    switched = SW(fk1)
    #print("after SW bits: "+str(switched))
    fk2 = funcFk(switched,subKeys[1])
    #print("after fk2 bits: "+str(fk2))
    ipInv = ipfunc(fk2,False)
    #print("after ipInv bits: "+ str(ipInv))

    return ipInv

def sdesDecryption(eightbitcypher,tenbitkey):
    subKeys = keygenerating(tenbitkey)
    ipBits = ipfunc(eightbitcypher,True)
    fk2 = funcFk(ipBits,subKeys[1])
    switched = SW(fk2)
    fk1 = funcFk(switched,subKeys[0])
    ipInv = ipfunc(fk1,False)

    return ipInv

def triplesdesEnc(eightbitplain,key1,key2):
    b1 = sdesEncryption(eightbitplain,key1)
    b2 = sdesDecryption(b1,key2)
    b3 = sdesEncryption(b2,key1)
    return b3

def triplesdesDec(eightbitciper,key1,key2):
    temp1 = sdesDecryption(eightbitciper,key1)
    temp2 = sdesEncryption(temp1,key2)
    temp3 = sdesDecryption(temp2,key1)
    return temp3


keys = [[0,0,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,1,1,1,0],[1,1,1,0,0,0,1,1,1,0],[1,1,1,1,1,1,1,1,1,1]]
plain = [[1,0,1,0,1,0,1,0],[1,0,1,0,1,0,1,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0]]

#print(sdesEncryption(plain[3],keys[3]))

task1keys = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1],[0,0,1,0,0,1,1,1,1,1],[0,0,1,0,0,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[1,0,0,0,1,0,1,1,1,0],[1,0,0,0,1,0,1,1,1,0]]
task1plain = [[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,0,0],[1,0,1,0,0,1,0,1]]
task1cipher = [[0,0,0,0,1,1,1,1],[0,1,0,0,0,0,1,1],[0,0,0,1,1,1,0,0],[1,1,0,0,0,0,1,0]]

"TASK 3"

def createBruteKeys():
    allkeys = []
    for i in range(1024):
        binaries = bin(i).replace("0b","")
        binaries = list(binaries)
        while(len(binaries)<10):
            binaries.insert(0,0)
        for i in range(len(binaries)):
            binaries[i] = int(binaries[i])
        allkeys.append(binaries)
    return allkeys

def splitTXT(inputText):
    text = []
    n = 8
    length = len(inputText)
    stops = int(length/n)
    for x in range(stops):
        text.append(list(ctx1[x*n:(x+1)*n]))
        print(x)
    return text


def crackSDES(cipherbits):
    text = splitTXT(cipherbits)
    keys = createBruteKeys()
    for keyx in keys:
        possText = []
        for letterbits in text:
            ltrbit = sdesDecryption(letterbits,keyx) 
            numbBit = 1*ltrbit[7]+2*ltrbit[6]+4*ltrbit[5]+8*ltrbit[4]+16*ltrbit[3]+32*ltrbit[2]+64*ltrbit[1]+128*ltrbit[0]
            if(numbBit<97 or numbBit>122): #97-122 because small letters
                break #Stop as early as possible with wrong ones
            possText.append(chr(numbBit))
        if len(possText)==len(text):
            return keyx,possText 

def crackTripleSDES(cipherbits):
    splitted = splitTXT(cipherbits)
    keys1 = createBruteKeys()
    keys2 = keys1
    for k1 in keys1 :
        for k2 in keys2:
            decryptTxt = []
            boolTest = True
            for ltr in splitted:

                ltrbit = triplesdesDec(ltr,k1,k2)
                numbBit = 1*ltrbit[7]+2*ltrbit[6]+4*ltrbit[5]+8*ltrbit[4]+16*ltrbit[3]+32*ltrbit[2]+64*ltrbit[1]+128*ltrbit[0]
                if(numbBit<97 or numbBit>122):
                    boolTest = False
                    break
                decryptTxt.append(chr(numbBit))
            if(boolTest):
                return k1,k2,decryptTxt


"Added functionality for assignment 2"

def intToTenBitArray(number):
    binaryStr = format(number,"010b")
    outputArr = []
    for b in binaryStr:
        outputArr.append(int(b))
    return outputArr


def stringToArr(bitString):
    outputArr = [None]*len(bitString)
    for b in range(len(bitString)):
        outputArr[b] = bitString[b]
    return outputArr

def BBSrand(seed,length):
    p = 11
    q = 23
    M = p*q
    outputNumb = ""
    x = seed
    for i in range(length):
        x = ((x ** 2) % M)
        if (x % 2) == 0:
            outputNumb += "0"
        else:
            outputNumb += "1"
    return outputNumb

def encryptString(InpString,key):
    byteArr = []
    for l in InpString:
        byteArr.append(format(ord(l),"08b")) #creates 8 bit value for each letter in inputstring with method ord() and format() in tandem

    encString = ""
    for byte in byteArr:
        temp = sdesEncryption(stringToArr(byte),key)
        for b in temp:
            encString += str(b)

    return encString


def decryptString(encString,key):
    decryptedString = ""
    tempArr = []
    i = 0
    in2 = 0
    for strBits in encString:

        if i==7:
            tempArr.append(strBits)
            in2 += 1
            #print(in2)
            decryptArr = sdesDecryption(tempArr,key)
            bStr = ""
            for e in decryptArr:
                bStr += str(e)
            decryptedString += str(chr(int(bStr,2)))
            tempArr=[]
            i=0
        else:
            tempArr.append(strBits)
            i+=1
    return decryptedString
