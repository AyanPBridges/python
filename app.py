import token

from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html",
                           )

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',port=8080)

def getInfo(network, address):
    url = "https://solana-gateway.moralis.io/nft/" + network + "/" + address + "/metadata"
    headers = {
        "accept": "application/json",
        "X-API-Key": "zUMibjOPQDAHs4wtYnhqwGNJUXGXAOwlNIO8VtajphV24cLA0xfTzxq3HRdOUHMx"
    }
    response = requests.get(url, headers=headers)
    return response
#example address = 8X6h5iqPik8FXP8kY3dDhEdMJjG2HUcmRfqoqGxQWXNc


#netw = str(input("Network: "))
#addr = str(input("Address: "))
#print(getInfo(netw, addr))