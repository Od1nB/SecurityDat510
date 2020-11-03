from flask import Flask
import requests
import hashlib
import random

app = Flask(__name__)
q = 10009 #shared prime q
a = 337 #shared a generator

privKey = 27
publicKey = pow(a,privKey,q)


def gcd(a,b):
    if a > b: 
        small = b 
    else: 
        small = a 
    for i in range(1, small+1): 
        if((a % i == 0) and (b % i == 0)): 
            gcd = i     
    return gcd

def generateK(qprime):
    number = random.randint(2,(q-1))
    while(gcd(qprime-1,number)!= 1):
        number = random.randint(2,(q-1))
    return number


@app.route("/")
def start():
    return "This is alice"

@app.route("/getpub")
def getpub():
    #a route so that the public key is easily accessedx
    return str(publicKey)


@app.route("/getinp")
def getInp():
    #f = open("data.txt","r")
    data = input("Enter a message to send to Bob: ")
    #data = f.read()
    hasher = hashlib.sha256(data.encode()) #Hashing with the seed as the data from the document
    hashData = hasher.hexdigest()
    liste = []
    while len(hashData)>0:
        liste.append(int(hashData[:3],16))
        hashData = hashData[3:]
    K = generateK(q)
   

    print(hashData)
    S1 = pow(a,K,q)
    Kinv = pow(K,-1,(q-1))

    S2 = ""
    for x in range(len(liste)):
        sTemp =  Kinv * (liste[x]-privKey*S1)
        S2 += str("{:04}".format(int(sTemp % (q-1))))
        S2 += "-"
    S2 = S2[:len(S2)-1]
  
    return str(S1)+"//"+str(S2) + "//" + str(data)

@app.route("/getDoc")
def getDoc():

        #hasher = hashlib.md5()
        #V1 = a ** m % q
        #V2 = (publickey ** S1) * (S1 **(all S2[i] % q))
        bobSend = requests.get("http://127.0.0.1:80/getinp")
        S1, S2str, message = str(bobSend.text).split("//")
        S1 = int(S1)
        S2 = S2str.split("-")

        dataHashed = hashlib.sha256(message.encode())
        hashNumbers = dataHashed.hexdigest()
        splittedHash = []
        while len(hashNumbers)>0:
            splittedHash.append(int(hashNumbers[:3],16))
            hashNumbers = hashNumbers[3:]
        print(splittedHash)

        V1 = ""
        for x in splittedHash:
            V1 += str(pow(a,x,q))
        print(V1)

        publicBob = int(requests.get("http://127.0.0.1:80/getpub").text)
        V2 = ""
        for s in S2:
            V2 += str((pow(publicBob,S1))*(pow(S1,int(s))) % q)
        print(V2)
        check = False
        if V1 == V2:
            check = True
        outstr = "The message was sent by bob: "+ str(check)
        


        return outstr 






if __name__ == "__main__":
    app.run(debug=True,port=5000)