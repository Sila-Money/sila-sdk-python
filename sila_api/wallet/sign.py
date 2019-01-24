from web3.auto import w3
from eth_account.messages import defunct_hash_message


def signMessage(msg,private_key):
    message_hash = defunct_hash_message(text=msg)
    signed_message = w3.eth.account.signHash(message_hash, private_key=private_key)
    return signed_message.signature.hex()