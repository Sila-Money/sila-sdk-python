from eth_account import Account
from eth_utils import keccak
import json

from typing import Dict, Union
from web3 import Web3


class EthWallet:

    @staticmethod
    def create(entropy=''):
        """Create an Ethereum wallet for a user.

        This will generate a private key and ethereum address, that can be used for transaction,
        however this not a recommended way to create your wallets
        Args:
        entropy : provide randomness to generate the wallet
        Returns:
        tuple: response body with ethereum address and private key
        """
        account = Account.create(entropy)
        return {"eth_private_key": Web3().to_hex(account._private_key), "eth_address": account.address}

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
        if isinstance(msg, str):
            encoded_message = msg.encode('utf-8')
        else:
            encoded_message = (json.dumps(msg)).encode("utf-8")
        encrypted = keccak(encoded_message)
        message_hash = Web3.to_hex(encrypted)[2:]
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
        if isinstance(msg, str):
            encoded_message = msg.encode('utf-8')
        else:
            encoded_message = (json.dumps(msg)).encode("utf-8")
        encrypted = keccak(encoded_message)
        message_hash = Web3.to_hex(encrypted)[2:]
        return Account._recover_hash(message_hash, signature=sign)
