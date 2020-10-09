from flask import Flask
import requests

app = Flask(__name__)
z = 953
pubg = 3
prvI = 9
publicKey = ((pubg ** prvI) % z)

@app.route("/")
def start():
    return "This is alice"

@app.route("/getpub")
def getpub():
    #make the public key and send it
    print(publicKey)
    return str(publicKey)

@app.route("/getmsg")
def getmsg():
    bobpublic = requests.get("http://127.0.0.1:80/getpub")
    bobInt = int(bobpublic.text)

    #send encrypt msg back
    return str(bobpublic.text) + str(publicKey)



if __name__ == "__main__":
    app.run(debug=True,port=5000)