from flask import Flask
import requests

app = Flask(__name__)
z = 953
pubg = 4
prvI = 6
publicKey = ((pubg ** prvI) % z)
sharedKey = None

@app.route("/")
def start():
    return "This is bob"

@app.route("/getpub")
def getpub():
    #make the public key and send it
    print(publicKey)
    #sharedKey = publicKey ** secretInt) % publicPrime)

    return str(publicKey)

@app.route("/getmsg")
def getmsg():
    bobpublic = requests.get("http://127.0.0.1:5000/getpub")
    bobInt = int(bobpublic.text)

    #send encrypt msg back
    return str(bobpublic.text) + str(publicKey)



if __name__ == "__main__":
    app.run(debug=True,port=80)