"""Test configuration constants for the Sila API Python SDK tests."""
import string
import random

from silasdk import EthWallet
from silasdk.client import App


letters = string.ascii_lowercase
strng = ''.join(random.choice(letters) for i in range(10))
strng_2 = ''.join(random.choice(letters) for i in range(10))
strng_3 = ''.join(random.choice(letters) for i in range(10))
strng_4 = ''.join(random.choice(letters) for i in range(10))
strng_5 = ''.join(random.choice(letters) for i in range(10))
strng_6 = ''.join(random.choice(letters) for i in range(10))


app_hanlde = "arc_sandbox_test_app01"
app_private_key = "9c17e7b767b8f4a63863caf1619ef3e9967a34b287ce58542f3eb19b5a72f076"
user_handle = strng
user_handle_2 = strng_2
business_handle = strng_3
instant_handle = strng_4
basic_individual_handle = strng_5
business_handle_2 = strng_6

#SANDBOX
business_uuid = "9f280665-629f-45bf-a694-133c86bffd5e"

app = App("sandbox", app_private_key, app_hanlde)

eth = EthWallet.create()
eth_address = eth["eth_address"]
eth_private_key = eth["eth_private_key"]

eth_2 = EthWallet.create()
eth_address_2 = eth_2["eth_address"]
eth_private_key_2 = eth_2["eth_private_key"]

eth_3 = EthWallet.create()
eth_address_3 = eth_3["eth_address"]
eth_private_key_3 = eth_3["eth_private_key"]

eth_4 = EthWallet.create()
eth_address_4 = eth_4.get('eth_address')
eth_private_key_4 = eth_4.get('eth_private_key')

eth_5 = EthWallet.create()
eth_address_5 = eth_5.get('eth_address')
eth_private_key_5 = eth_5.get('eth_private_key')

eth_6 = EthWallet.create()
eth_address_6 = eth_6.get('eth_address')
eth_private_key_6 = eth_6.get('eth_private_key')

wallet = EthWallet.create()
wallet_address = wallet["eth_address"]
wallet_private_key = wallet["eth_private_key"]
verification_signature = EthWallet.signMessage(
    wallet_address, wallet_private_key)
wallet_address_signed_verified = EthWallet.verifySignature(
    wallet_address, verification_signature)
