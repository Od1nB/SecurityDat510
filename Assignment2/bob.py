from flask import Flask
import requests
from Tools import SDES as sdes
#import SecurityDat510.Assignment2.Tools.SDES as sdes

app = Flask(__name__)
z = 953
pubg = 4
prvI = 6
publicKey = ((pubg ** prvI) % z)
sharedKey = None
msg = "eyo this is me"

@app.route("/")
def start():
    return "This is bob"

@app.route("/getpub")
def getpub():
    #make the public key and send it
    #print(publicKey)
    #sharedKey = publicKey ** secretInt) % publicPrime)

    return str(publicKey)

@app.route("/getmsg")
def getmsg():
    alicepublic = requests.get("http://127.0.0.1:5000/getpub")
    aliceInt = int(alicepublic.text)
    sharedKey = ((aliceInt ** prvI) % z)
    print("shared key of bob is "+str(sharedKey))

    encryptedGet = requests.get("http://127.0.0.1:5000/sendmsg")
    encryptedMsg = str(encryptedGet.text)

    decryptedMsg = sdes.decryptString(encryptedMsg,sdes.intToTenBitArray(sharedKey))
    #send encrypt msg back
    return str(alicepublic.text) + str(publicKey)

@app.route("/sendmsg")
def sendmsg():
    alicepublic = requests.get("http://127.0.0.1:5000/getpub")
    aliceInt = int(alicepublic.text)
    sharedKey = ((aliceInt ** prvI) % z)
    encryptedMsg = sdes.encryptString(msg,sdes.intToTenBitArray(sharedKey))
    return encryptedMsg



if __name__ == "__main__":
    app.run(debug=True,port=80)