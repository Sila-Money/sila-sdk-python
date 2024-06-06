import unittest
from silasdk.wallet import Wallet
from tests.test_config import (app, eth_private_key, user_handle,
                               verification_signature, wallet_address, wallet_address_signed_verified)


class Test014RegisterWalletTest(unittest.TestCase):
    def test_register_wallet_200(self):
        payload = {
            "user_handle": user_handle,
            "wallet_verification_signature": verification_signature,
            "wallet": {
                "blockchain_address": wallet_address,
                "blockchain_network": "ETH",
                "nickname": "wallet_python_new",
                "default": True,
                "statements_enabled": True
            }
        }

        response = Wallet.registerWallet(app, payload, eth_private_key)
        self.assertTrue(response["statements_enabled"])
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

    def test_register_wallet_400(self):
        payload = {
            "user_handle": user_handle,
            "wallet_verification_signature": verification_signature,
            "wallet": {
                "blockchain_address": wallet_address_signed_verified,
                "blockchain_network": "ETH",
                "nicknames": "wallet_python",
                "default": True
            }
        }

        response = Wallet.registerWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_register_wallet_401(self):
        payload = {
            "user_handle": "",
            "wallet_verification_signature": verification_signature,
            "wallet": {
                "blockchain_address": wallet_address_signed_verified,
                "blockchain_network": "ETH",
                "nickname": "wallet_python",
                "default": True
            }
        }

        response = Wallet.registerWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_register_wallet_403(self):
        payload = {
            "user_handle": user_handle,
            "wallet_verification_signature": "",
            "wallet": {
                "blockchain_address": wallet_address_signed_verified,
                "blockchain_network": "ETH",
                "nickname": "wallet_python",
                "default": True
            }
        }

        response = Wallet.registerWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
