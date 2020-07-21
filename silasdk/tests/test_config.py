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

#
app_hanlde = "digital_geko_e2e.silamoney.eth"
app_private_key = os.environ.get("SILA_PRIVATE_KEY")
user_handle = strng
user_handle_2 = strng_2
business_handle = strng_3
business_uuid = "9f280665-629f-45bf-a694-133c86bffd5e"

#import os
app = App("SANDBOX", app_private_key, app_hanlde)

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

#
wallet = EthWallet.create()
wallet_address = wallet["eth_address"]
wallet_private_key = wallet["eth_private_key"]
verification_signature = EthWallet.signMessage(wallet_address, wallet_private_key)
wallet_address_signed_verified = EthWallet.verifySignature(wallet_address, verification_signature)
