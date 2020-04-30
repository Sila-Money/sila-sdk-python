import unittest

from silasdk.stellarwallet import Wallet
from silasdk.tests.test_config import *


class GetWalletTest(unittest.TestCase):
    def test_get_wallet_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = Wallet.getWallet(app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_get_wallet_400(self):
        payload = {
            "user_handle": "",
            "crypto": "ETHS"
        }

        response = Wallet.getWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_get_wallet_401(self):
        payload = {
            "user_handle": user_handle.replace("1", "2"),
            "crypto": "ETHS"
        }

        response = Wallet.getWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
