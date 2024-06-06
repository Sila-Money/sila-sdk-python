import unittest
from silasdk.wallet import Wallet
from tests.test_config import (
    app, eth_private_key, user_handle, wallet_private_key)


class Test018DeleteWalletTest(unittest.TestCase):
    def test_delete_wallet_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = Wallet.deleteWallet(app, payload, wallet_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

    def test_delete_wallet_400(self):
        payload = {
            "user_handle": '',
        }

        response = Wallet.deleteWallet(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_delete_wallet_401(self):
        payload = {
            "user_handle": user_handle
        }

        response = Wallet.deleteWallet(app, payload, '')
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
