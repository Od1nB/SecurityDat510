from flask import Flask
import requests
from Tools import SDES as sdes
#import SecurityDat510.Assignment2.Tools.SDES as sdes

app = Flask(__name__)
z = 953
pubg = 3
prvI = 9
publicKey = ((pubg ** prvI) % z)
sharedKey = None
msg = "This is alice saying hello"

@app.route("/")
def start():
    return "This is alice"

@app.route("/getpub")
def getpub():
    #make the public key and send it
    #print(publicKey)
    return str(publicKey)

@app.route("/getmsg")
def getmsg():
    bobpublic = requests.get("http://127.0.0.1:80/getpub")
    bobInt = int(bobpublic.text)
    sharedKey = ((bobInt ** prvI) % z)
    print("shared key of alice is "+str(sharedKey))

    encryptedGet = requests.get("http://127.0.0.1:80/sendmsg")
    encryptedMsg = str(encryptedGet.text)
    print(encryptedMsg)
    #print(sdes.intToTenBitArray(sharedKey))

    decryptedMsg = sdes.decryptString(encryptedMsg,sdes.intToTenBitArray(sharedKey))

    #send encrypt msg back
    return decryptedMsg

@app.route("/sendmsg")
def sendmsg():
    bobpublic = requests.get("http://127.0.0.1:80/getpub")
    bobInt = int(bobpublic.text)
    print(bobInt)
    print(type(bobInt))
    sharedKey = ((bobInt ** prvI) % z)
    encryptedMsg = sdes.encryptString(msg,sdes.intToTenBitArray(sharedKey))
    return encryptedMsg




if __name__ == "__main__":
    app.run(debug=True,port=5000)