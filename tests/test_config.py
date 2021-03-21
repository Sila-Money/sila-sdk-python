import string
import os
import random

from silasdk import EthWallet
from silasdk.client import App

'''

'''

#
letters = string.ascii_lowercase
strng = ''.join(random.choice(letters) for i in range(10))
strng_2 = ''.join(random.choice(letters) for i in range(10))
strng_3 = ''.join(random.choice(letters) for i in range(10))
strng_4 = ''.join(random.choice(letters) for i in range(10))
strng_5 = ''.join(random.choice(letters) for i in range(10))

#
app_hanlde = "digital_geko_e2e"
app_private_key = "e60a5c57130f4e82782cbdb498943f31fe8f92ab96daac2cc13cbbbf9c0b4d9e"
user_handle = strng
user_handle_2 = strng_2
business_handle = strng_3
instant_ach_handle = strng_4
basic_individual_handle = strng_5
business_uuid = "ec5d1366-b56c-4442-b6c3-c919d548fcb5"

app = App("sandbox", app_private_key, app_hanlde)

#
eth = EthWallet.create()
eth_address = eth["eth_address"]
eth_private_key = eth["eth_private_key"]


#
eth_2 = EthWallet.create()
eth_address_2 = eth_2["eth_address"]
eth_private_key_2 = eth_2["eth_private_key"]

#
eth_3 = EthWallet.create()
eth_address_3 = eth_3["eth_address"]
eth_private_key_3 = eth_3["eth_private_key"]

eth_4 = EthWallet.create()
eth_address_4 = eth_4.get('eth_address')
eth_private_key_4 = eth_4.get('eth_private_key')

eth_5 = EthWallet.create()
eth_address_5 = eth_5.get('eth_address')
eth_private_key_5 = eth_5.get('eth_private_key')

#
wallet = EthWallet.create()
wallet_address = wallet["eth_address"]
wallet_private_key = wallet["eth_private_key"]
verification_signature = EthWallet.signMessage(
    wallet_address, wallet_private_key)
wallet_address_signed_verified = EthWallet.verifySignature(
    wallet_address, verification_signature)
