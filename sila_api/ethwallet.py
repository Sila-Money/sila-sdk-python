from web3.auto import w3
from eth_account.messages import defunct_hash_message



class Wallet():


            def create():

                account=w3.eth.account.create()
                return ("This is not the recommended way to create your ethereum wallet",
                        {"private_key":account.privateKey.hex(),"eth_address":account.address})



            def signMessage(msg,private_key):

                message_hash = defunct_hash_message(text=str(msg))
                signed_message = w3.eth.account.signHash(message_hash, private_key=private_key)
                return signed_message.signature.hex()


