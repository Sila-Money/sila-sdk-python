#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
from silasdk import App
from silasdk import User
from silasdk import Transaction

#App private key,ENV and handle can be set as env variables if required

app1=App("TEST",'18B580BF02D42742D5D102CCB7E30DC15FF09D48046FF4B37EAFF3C30D5DBE6B',"tyagi1.silamoney.eth")

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='Joe')


@app.route('/checkHandle', methods = ['POST'])
def checkHandle():
    # read json + reply
    data = request.json
    result = json.dumps(User.checkHandle(app1,data))
    return result

@app.route('/register', methods = ['POST'])
def register():
    # read json + reply
    data = request.json
    result = json.dumps(User.register(app1,data))
    return result


@app.route('/requestKyc', methods = ['POST'])
def requestKyc():
    data = request.json
    result = json.dumps(User.requestKyc(app1,data))
    return result



@app.route('/checkKyc', methods = ['POST'])
def checkKyc():
    # read json + reply
    data = request.json
    result = json.dumps(User.checkKyc(app1,data))
    return result



@app.route('/linkAccount', methods = ['POST'])
def linkAccount():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    data1=json.dumps(data.decode("utf-8"))
    result = json.dumps(User.linkAccount(app1,data,data1["private_key"]))
    return result

#Never transmit private keys over the network in the request body

@app.route('/getAccounts', methods = ['POST'])
def getAccounts():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    print(private_key)
    result = json.dumps(User.getAccounts(app1,data,private_key))
    return result



@app.route('/getTransactions', methods = ['POST'])
def getTransactions():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(User.getTransactions(app1,data,private_key))
    return result


@app.route('/issueSila', methods = ['POST'])
def issueSila():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(Transaction.issueSila(app1,data,private_key))
    return result


@app.route('/redeemSila', methods = ['POST'])
def redeemSila():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(Transaction.redeemSila(app1,data,private_key))
    return result



@app.route('/transferSila', methods = ['POST'])
def transferSila():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(Transaction.transferSila(app1,data,private_key))
    return result





if __name__ == '__main__':
	# run!
	app.run(debug=True)
