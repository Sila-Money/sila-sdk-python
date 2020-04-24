import unittest

from silasdk.stellarwallet import Wallet
from silasdk.tests.test_config import *


class UpdateWalletTest(unittest.TestCase):
    def test_update_wallet_200(self):
        payload = {
            "user_handle": user_handle,
            "nickname": "wallet_python_updated",
            "crypto": "ETH",
            "default": True
        }

        response = Wallet.getWallet(app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_update_wallet_400(self):
        payload = {
            "user_handle": user_handle,
            "nickname": "wallet_python_updated",
            "default": True,
            "crypto": "ETHS",
            "blockchain_address": "0x00000"
        }

        response = Wallet.getWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_update_wallet_401(self):
        payload = {
            "user_handle": "",
            "nickname": "wallet_python_updated",
            "crypto": "ETH",
            "default": True
        }

        response = Wallet.getWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
