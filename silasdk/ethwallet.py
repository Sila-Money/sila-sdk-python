from eth_account import Account
import sha3, _pysha3
import json

from typing import Dict, Union


class EthWallet:

    @staticmethod
    def create(entropy=''):
        """Create an Ethereum wallet for a user.

        This will generate a private key and ethereum address, that can be used for trasaction,
        however this not a recommended way to create your wallets
        Args:
        entropy : provide randomness to gnerate the wallet
        Returns:
        tuple: response body with ethereum address and private key
        """
        account = Account.create(entropy)
        return {"eth_private_key": account.privateKey.hex(), "eth_address": account.address}

    @staticmethod
    def signMessage(msg: Union[str, Dict], key=None):
        """Sign the message using an Ethereum private key.

        This method signs the message for the user authentication mechanism
        Args:
        msg: message to be signed
        private_key: the key can be an app key or a user key used to sign the message
        Returns:
        string: a signed message
        """
        k = _pysha3.keccak_256()
        if isinstance(msg, str):
            encoded_message = msg.encode('utf-8')
        else:
            encoded_message = (json.dumps(msg)).encode("utf-8")
        k.update(encoded_message)
        message_hash = k.hexdigest()
        if key is not None:
            signed_message = Account.signHash(message_hash, key)
            sig_hx = signed_message.signature.hex()
            return str(sig_hx.replace("0x", ""))

        else:
            return " "

    @staticmethod
    def verifySignature(msg: Union[str, Dict], sign):
        """Verify the message signature.

        This method signs the message for the user authentication mechanism
        Args:
        msg: original message
        sign : the signed hash obtained after signing the message with private key
        Returns:
        string: returns the Ethereum address corresponding to the private key the message was signed with
        """
        k = _pysha3.keccak_256()
        if isinstance(msg, str):
            encoded_message = msg.encode('utf-8')
        else:
            encoded_message = (json.dumps(msg)).encode("utf-8")
        k.update(encoded_message)
        message_hash = k.hexdigest()
        return Account.recoverHash(message_hash, signature=sign)
