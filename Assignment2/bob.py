from flask import Flask
import requests
from Tools import SDES as sdes

app = Flask(__name__)
z = 953 #Sophie Germain prime: 2p +1
pubg = 3 #Generator
prvI = 6
publicKey = ((pubg ** prvI) % z)
sharedKey = None
msg = "eyo this is bob"

@app.route("/")
def start():
    return "This is bob"

@app.route("/getpub")
def getpub():
    #a route so that the public key is easily accessed
    return str(publicKey)

@app.route("/getmsg")
def getmsg():
    alicepublic = requests.get("http://127.0.0.1:5000/getpub")
    aliceInt = int(alicepublic.text)
    sharedKey = ((aliceInt ** prvI) % z)
    sharedK = sdes.BBSrand(sharedKey,10)
    print("shared key of bob after BBS is "+str(sharedK))

    encryptedGet = requests.get("http://127.0.0.1:5000/sendmsg")
    encryptedMsg = str(encryptedGet.text)

    decryptedMsg = sdes.decryptString(encryptedMsg,sdes.stringToArr(sharedK))
    #send encrypt msg back
    return decryptedMsg

@app.route("/sendmsg")
def sendmsg():
    alicepublic = requests.get("http://127.0.0.1:5000/getpub")
    aliceInt = int(alicepublic.text)
    sharedKey = ((aliceInt ** prvI) % z)
    sharedK = sdes.BBSrand(sharedKey,10)
    encryptedMsg = sdes.encryptString(msg,sdes.stringToArr(sharedK))
    return encryptedMsg



if __name__ == "__main__":
    app.run(debug=True,port=80)