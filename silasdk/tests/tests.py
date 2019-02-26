import unittest
import string
import random
from silasdk.user import User
from silasdk.client import App
from silasdk.ethwallet import EthWallet
letters = string.ascii_lowercase

strng= ''.join(random.choice(letters) for i in range(10))

app_hanlde=strng+".silamoney.eth"
user_handle=strng+".silamoney.eth"
app_private_key=EthWallet.create("run my tests")[1]["private_key"]
app=App("TEST",app_private_key,app_private_key)

print (User.checkHandle(app,user_handle))





