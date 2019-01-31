from web3.auto import w3
from eth_account.messages import defunct_hash_message


# Create an ethereum public private-key pair, sign the message and verify signatures for etheruem address

class EthWallet():


            def create(entropy):

                    account=w3.eth.account.create(entropy)
                    return ("This is not the recommended way to create your ethereum wallet",
                            {"private_key":account.privateKey.hex(),"eth_address":account.address})



            def signMessage(msg,private_key):

                    message_hash = defunct_hash_message(text=str(msg))
                    signed_message = w3.eth.account.signHash(message_hash, private_key=private_key)
                    sig_hx=signed_message.signature.hex()
                    return str(sig_hx.replace("0x",""))

            
            def verifySignature(msg,sign):
                    
                    message_hash = defunct_hash_message(text=str(msg))
                    return w3.eth.account.recoverHash(message_hash,signature=sign)








