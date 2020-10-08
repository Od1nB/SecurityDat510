from flask import Flask
import Part2_SDES as SDES

app = Flask(__name__)

@app.route("/")
def start():
    return "This is the landing page and there has not been inputted any bits"

@app.route("/<cipherbits>")
def hello(cipherbits):
    k1 = [1,0,0,0,1,0,1,1,1,0] #"1000101110"
    k2 = [0,1,1,0,1,0,1,1,1,0] #"0110101110"
    list1 = SDES.splitTXT(cipherbits)
    plain =""
    for eightbits in list1:
        ltrbit = SDES.triplesdesDec(eightbits,k1,k2)
        numbBit = 1*ltrbit[7]+2*ltrbit[6]+4*ltrbit[5]+8*ltrbit[4]+16*ltrbit[3]+32*ltrbit[2]+64*ltrbit[1]+128*ltrbit[0]
        plain += chr(numbBit)
    return plain

if __name__ == "__main__":
    app.run(debug=True)


