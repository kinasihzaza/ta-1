from flask import json, Flask, request
import test
app = Flask(__name__)

# encoding: utf-8
import sys
import xxtea
import unittest

instanceXxtea = test.TestXXTEA()


@app.route('/', methods=['GET','POST'])
def root():
    return "Hallo"

@app.route('/sample', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

@app.route('/en', methods=['POST'])
def encrypt_method():
    if request.headers['Content-Type'] == 'application/json':
        print "Request JSON : "+str(request.data)
        '''ALGO
            1) Bongkar
            2) Masukin Variable
            3) Masukin Variable Ke Method Enkrip
            4) Nerima Return Dari Method Enkrip
            5) Return ke Client dalam bentuk JSON
        '''
        ## Bongkar Bungkusan dari Client dan dimasukin variable ##
        payLoadFromClient = json.loads(request.data)
        varSender = payLoadFromClient['from']
        varReceiver = payLoadFromClient['to']
        varKey = payLoadFromClient['data'][0]['key']
        varText = payLoadFromClient['data'][0]['text']

        ## Panggil Instance, Masukin ke method ##
        resultFromEncrypMethod = instanceXxtea.encrypt(varKey, varText)
        print resultFromEncrypMethod

        returnForClient = {'from':varSender, 'to':varReceiver, 'data':[
            {'text':resultFromEncrypMethod}
        ]}

        return "WebService Encrypted JSON : "+json.dumps(returnForClient)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

@app.route('/de', methods=['POST'])
def decrypt_method():
    if request.headers['Content-Type'] == 'application/json':
        print "Request JSON : "+str(request.data)
        '''ALGO
            1) Bongkar
            2) Masukin Variable
            3) Masukin Variable Ke Method Dekrip
            4) Nerima Return Dari Method Dekrip
            5) Return ke Client dalam bentuk JSON
        '''
        ## Bongkar Bungkusan dari Client dan dimasukin variable ##
        payLoadFromClient = json.loads(request.data)
        varSender = payLoadFromClient['from']
        varReceiver = payLoadFromClient['to']
        varKey = payLoadFromClient['data'][0]['key']
        varText = payLoadFromClient['data'][0]['text']

        ## Panggil Instance, Masukin ke method ##
        ## Masukin Result ke variable
        resultFromDecryptMethod = instanceXxtea.decrypt(varKey, varText)

        ## Check Hasil
        print resultFromDecryptMethod

        ## Bungkus dalam bentuk JSON
        returnForClient = {'from':varSender, 'to':varReceiver, 'data':[
            {'text':resultFromDecryptMethod}
        ]}

        ## Kirim Ke Client
        return "WebService Decrypted JSON : "+json.dumps(returnForClient)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
	app.run(
		host="0.0.0.0",
		port=int(6000),
        debug=True,
        threaded=True
	)
