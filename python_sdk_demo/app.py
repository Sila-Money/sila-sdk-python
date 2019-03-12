#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
from silasdk import App
from silasdk import User
from silasdk import Transaction

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

#Never transmit private keys over the network

@app.route('/linkAccount', methods = ['POST'])
def linkAccount():
    # read json + reply
    data = request.data
    data1=json.dumps(data.decode("utf-8"))
    result = json.dumps(User.linkAccount(app1,data,data1["private_key"]))
    return result

#Never transmit private key over the network

@app.route('/getAccounts', methods = ['POST'])
def getAccounts():
    # read json + reply
    data = request.json
    private_key=data["private_key"]
    print(private_key)
    result = json.dumps(User.getAccounts(app1,data,private_key))
    return result



@app.route('/getTransactions', methods = ['POST'])
def getTransactions():
    # read json + reply
    data = request.json
    result = json.dumps(User.getTransactions(app1,data))
    return result


@app.route('/issueSila', methods = ['POST'])
def issueSila():
    # read json + reply
    data = request.json
    result = json.dumps(Transaction.issueSila(app1,data))
    return result


@app.route('/redeemSila', methods = ['POST'])
def redeemSila():
    # read json + reply
    data = request.json
    result = json.dumps(Transaction.redeemSila(app1,data))
    return result



@app.route('/transferSila', methods = ['POST'])
def transferSila():
    # read json + reply
    data = request.json
    result = json.dumps(Transaction.transferSila(app1,data))
    return result





if __name__ == '__main__':
	# run!
	app.run(debug=True)
