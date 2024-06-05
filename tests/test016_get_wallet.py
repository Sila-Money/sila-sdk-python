import unittest, silasdk

from tests.test_config import *


class Test016GetWalletTest(unittest.TestCase):
    def test_get_wallet_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = silasdk.Wallet.getWallet(app, payload, eth_private_key)
        self.assertTrue(response["wallet"]["statements_enabled"])
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["sila_available_balance"])
        self.assertIsNotNone(response["sila_pending_balance"])

    def test_get_wallet_400(self):
        payload = {
            "user_handle": "",
            "crypto": "ETHS"
        }

        response = silasdk.Wallet.getWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_get_wallet_401(self):
        payload = {
            "user_handle": user_handle.replace("1", "2"),
            "crypto": "ETHS"
        }

        response = silasdk.Wallet.getWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
