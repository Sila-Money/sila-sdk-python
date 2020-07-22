import unittest, silasdk

from silasdk.tests.test_config import *

class Test018DeleteWalletTest(unittest.TestCase):
    def test_delete_wallet_200(self):
        payload = {
            "user_handle": user_handle,
            "crypto": "ETH"
        }

        response = silasdk.Wallet.getWallet(app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_delete_wallet_400(self):
        payload = {
            "user_handle": user_handle,
            "crypto": "ETHS",
            "blockchain_address": "0x0000000A"
        }

        response = silasdk.Wallet.getWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_delete_wallet_401(self):
        payload = {
            "user_handle": "",
            "crypto": "ETH"
        }

        response = silasdk.Wallet.getWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
