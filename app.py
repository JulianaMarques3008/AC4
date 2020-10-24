import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')

def fibonacci():
    p = 1
    a = 0
    limite = 50
    f = 0
    resp = "0,"
    
    while (f < limite):
        temp = p
        p = p + a
        a = temp
        f = f + 1
        resp+= str(p)+","

    return resp

if __name__== "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
