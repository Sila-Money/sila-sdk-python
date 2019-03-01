from web3.auto import w3
from eth_account.messages import defunct_hash_message


class EthWallet():


        def create(entropy):
                """create an ethereum wallet for user
                This will generate a private key and ethereum address, that can be used for trasaction,
                however this not a recommended way to create your wallets
                Args:
                entropy : provide randomness to gnerate the wallet
                Returns:
                tuple: response body with ethereum address and private key
                """
                account=w3.eth.account.create(entropy)
                return {"eth_private_key":account.privateKey.hex(),"eth_address":account.address}


        
        def signMessage(msg,*args):
                """Sign the message using an ethereum private key
                This method signs the message for the user authentication mechanism
                Args:
                msg: message to be signed 
                private_key: the key can be an app key or a user key used to sign the message
                Returns:
                string: a signed message
                """
                message_hash = defunct_hash_message(text=str(msg))
                for arg in args:
                        signed_message = w3.eth.account.signHash(message_hash, private_key=arg)
                        sig_hx=signed_message.signature.hex()
                        return str(sig_hx.replace("0x",""))
                if not args:
                        return " "


        
        def verifySignature(msg,sign):
                """Verify the message signature 
                This method signs the message for the user authentication mechanism
                Args:
                msg: original message
                sign : the signed hash obtained after signing the message with private key
                Returns:
                string: returns the ethereum address corresponding to the private key the message was signed with
                """
                message_hash = defunct_hash_message(text=str(msg))
                return w3.eth.account.recoverHash(message_hash,signature=sign)








