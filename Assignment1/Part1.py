import time as t

ciphertext = "BQZRMQ KLBOXE WCCEFL DKRYYL BVEHIZ NYJQEE BDYFJO PTLOEM EHOMIC UYHHTS GKNJFG EHIMK NIHCTI HVRIHA RSMGQT RQCSXX CSWTNK PTMNSW AMXVCY WEOGSR FFUEEB DKQLQZ WRKUCO FTPLOT GOJZRI XEPZSE ISXTCT WZRMXI RIHALE SPRFAE FVYORI HNITRG PUHITM CFCDLA HIBKLH RCDIMT WQWTOR DJCNDY YWMJCN HDUWOF DPUPNG BANULZ NGYPQU LEUXOV FFDCEE YHQUXO YOXQUO DDCVIR RPJCAT RAQVFS AWMJCN HTSOXQ UODDAG BANURR REZJGD VJSXOO MSDNIT RGPUHN HRSSSF VFSINH MSGPCM ZJCSLY GEWGQT DREASV FPXEAR IMLPZW EHQGMG WSEIXE GQKPRM XIBFWL IPCHYM OTNXYV FFDCEE YHASBA TEXCJZ VTSGBA NUDYAP IUGTLD WLKVRI HWACZG PTRYCE VNQCUP AOSPEU KPCSNG RIHLRI KUMGFC YTDQES DAHCKP BDUJPX KPYMBD IWDQEF WSEVKT CDDWLI NEPZSE OPYIW"
ciphertext2 = "BQZRMQ KLAYAV AYITET EOFGWT EALRRD HNIFML BIHHQY XXEXYV LPHFLW UOJILE GSDLKH BZGCTA LHKAIZ BIOIGK SZXLZS UTCPZW JHNPUS MSDITN OSKSJI EOKVIL BKMSZB XZOEHA KTAWXP WLUEJM AIWGLR TZLVHZ SATVQI HZWAXX ZXDCIV TMLBIQ RWZMLB VNGVQK AIZBXZ HVVMMA MJLRIW GKITZL VHZRRV YCBTVM FVOIYE FSKGKJ AVWHUV BUHZSA EFLHMQ HHVSGZ XIKYTS YZXUUC KBTOGU VABLDP BGJCGF NLIIYA HJFWGG PSCPVA ZEASME MLGOYR CGFXVG EJTTTW TSAAIL QFKEEP CPULXW WZRLVI VVYUMS MSILRI IBLWJI TKWUXZ GUZEJG DUCQEE QEOBTP SIHTGW UALVMA ILTAEZ TFLDPE IVEGYH PLZRTC YJVYGX ABFNPQ XLCEYA RGIFCC WHBGIF WSYLBZ MDWFPX KZSYCY APJTFR CKTYYU YICYLR ZALETS DWHMGR PTTGUW CGFNTB JTRNWR AADNPQ XLTBGP RZMJTF KGTSPV DTVAPE ZPRIP"
engAlpha = {'A':0.08167, 'B':0.01492, 'C':0.02782, 'D':0.04253, 'E':0.12702, 'F':0.0228, 'G':0.02015, 'H':0.06094, 'I':0.06996, 'J':0.00153, 'K':0.00772, 'L':0.04025, 'M':0.02406, 'N':0.06759, 'O':0.07507, 'P':0.01929, 'Q':0.00095, 'R':0.05987, 'S':0.06327, 'T':0.09056, 'U':0.02758, 'V':0.00978, 'W':0.0236, 'X':0.0015, 'Y':0.01974, 'Z':0.00074}
Keywords = [["A","B","C"],["A","B","C","D","E"],["A","B","C","D","E","F","G","H","I"],["A","B","C","D","E","F","G","H","I","J","K","L","M"]] # 3, 5, 9, 13
plainTxt = "ANORIGINALMESSAGEISKNOWNASTHEPLAINTEXTWHILETHECODEDMESSAGEISCALLEDTHECIPHERTEXTTHEPROCESSOFCONVERTINGFROMPLAINTEXTTOCIPHERTEXTISKNOWNASENCIPHERINGORENCRYPTIONRESTORINGTHEPLAINTEXTFROMTHECIPHERTEXTISDECIPHERINGORDECRYPTIONTHEMANYSCHEMESUSEDFORENCRYPTIONCONSTITUTETHEAREAOFSTUDYKNOWNASCRYPTOGRAPHYSUCHASCHEMEISKNOWNASACRYPTOGRAPHICSYSTEMORACIPHERTECHNIQUESUSEDFORDECIPHERINGAMESSAGEWITHOUTANYKNOWLEDGEOFTHEENCIPHERINGDETAILSFALLINTOTHEAREAOFCRYPTANALYSISCRYPTANALYSISISWHATTHELAYPERSONCALLSBREAKINGTHECODETHEAREASOFCRYPTOGRAPHYANDCRYPTANALYSISTOGETHERARECALLEDCRYPTOLOGY"

"TASK 1/3"
ciphWithoutSpaces = "".join(ciphertext.split( ))
cip2withou ="".join(ciphertext2.split( ))

def combinations(ciph,size):
    output = []
    for i in range((len(ciph)-1)):
        output.append(ciph[i:i+size])
    return(output)

comboList = combinations(ciphWithoutSpaces,3)

#The most used 3word combo is prob THE so we will try to find this
comboOcc = {}
for n in comboList:
    if n in comboOcc.keys():
        comboOcc[n] += 1
    else:
        comboOcc[n] = 1
max_key = max(comboOcc, key=lambda k: comboOcc[k])
#most used 3word combo is "RIH"

#Find index of  T H E in cipherWithoutSpaves
indexOfTHE = []
for i in range(len(ciphWithoutSpaces)-1):
    if (ciphWithoutSpaces[i]=="H"):
        if (ciphWithoutSpaces[i-1]=="I"):
            if (ciphWithoutSpaces[i-2]=="R"):
                indexOfTHE.append(i-2)
                indexOfTHE.append(i-1)
                indexOfTHE.append(i)

#Find the diff in length between them
diffs = []
for i in range(len(indexOfTHE)-1,0,-3):
    if i==len(indexOfTHE)-1:
        numb = indexOfTHE[i]
    elif i==0:
        pass
    else:
        numb = indexOfTHE[i]
        diffs.append(numb-indexOfTHE[i])

diffs.sort()

#Find a common factor  70 160 200 490 -> 30 20 100 380 -> to find factor and one of theses is length of key
def findDivisors(n) :
    output = [] 
    i = 1
    while i <= n : 
        if (n % i==0) :
            output.append(i)
        i = i + 1
    return output
print(findDivisors(diffs[2]))

coFactors = []
for i in range(len(diffs)-1):
    if(i==0):
        coFactors = findDivisors(diffs[i])
    else:
        temp = findDivisors(diffs[i])
        for x in coFactors:
            if(x not in temp):
                coFactors.remove(x)

#Has to be 8 so we start there
#make 8 alphabets and then count the frequancy of each letter in them

def divOnLength(cipher, keylength):
    alphabet = {}
    for b in range(keylength):
        alphabet[b] = {}
    q = 0
    for i in range(len(cipher)):
        if (i%keylength==q):
            if (str(cipher[i]) in alphabet[q]):
                alphabet[q][cipher[i]]+=1
            else:
                alphabet[q][str(cipher[i])]=1
            q+=1
            if q>7: q = 0
    return alphabet

def chiSquared(dictList):
    sumKeys = []
    values_Alpha = [None]*len(dictList)
    for x in range(len(dictList)):
        for y in dictList[x].values():
            if values_Alpha[x]==None:
                values_Alpha[x] = y
            else:
                values_Alpha[x] += y 

    for i in range(len(dictList)):
        for x,y in dictList[i].items():
            dictList[i][x]=y/values_Alpha[i]
    

    for j in dictList:
        sumList = []
        sumDict = {}
        for i in range(26):
            summSumm = 0.0
            for letter,e in engAlpha.items():
                    letter = ord(letter)+i
                    if(letter > 90): #To ensure the letter is in between the right ASCII values, if not start from start of alphab
                        letter = chr(letter-26)
                    else:
                        letter = chr(letter)
                    
                    if letter in dictList[j]:
                        o = dictList[j][letter]
                        summSumm += ((o-e)**2)/e
                    else:
                        summSumm += ((-e)**2)/2
            sumList.append(summSumm)
            sumDict[summSumm] = chr(i + 65)
        key = sumDict[min(sumList)]
        sumKeys.append(key)
    return sumKeys

def decipher(ciphertext, keyword):
    for k in range(len(keyword)):
        keyWord[k] = ord(keyWord[k])-65
    txtplain = ""
    for i in range(len(ciphertext)):
        letterchi = ord(ciphertext[i])
        plainltr = letterchi- int(keyWord[i% len(keyWord)])
        if plainltr <65:
            plainltr+=26
        txtplain += chr(plainltr)
    
    return txtplain

alphabets = divOnLength(ciphWithoutSpaces,8)
keyWord = chiSquared(alphabets)
plain = decipher(ciphWithoutSpaces,keyWord)
#print(plain)

#print(decipher(cip2withou,keyWord))

"TASK 2"
def enchipfer(plaintext, keyNr):
    plainList = list(plaintext)
    keyshift = []
    for letter in Keywords[keyNr]:
        keyshift.append(ord(letter)-65)

    lengthKey = len(Keywords[keyNr])
    ciphertxt =""
    n=0

    for letter in plainList:
        if n == lengthKey:
            n=0
        ltrNumber = ord(letter)+keyshift[n]
        if ltrNumber>90:
            ltrNumber += 26
            ciphertxt += chr(ltrNumber)
            n +=1
    return ciphertxt

def checkTime(keyNr):
    cipherCheck = enchipfer(plainTxt,keyNr)

    time_start = t.time()

    kW = chiSquared(cipherCheck)
    pln = decipher(cipherCheck,kW)
    
    time_stop = t.time()
    return time_stop-time_start
