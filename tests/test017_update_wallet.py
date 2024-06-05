import unittest
from silasdk.wallet import Wallet

from tests.test_config import (app, user_handle, eth_private_key)


class Test017UpdateWalletTest(unittest.TestCase):
    def test_update_wallet_200(self):
        nickname = 'wallet_python_updated'
        payload = {
            "user_handle": user_handle,
            "nickname": nickname,
            "default": True,
            "statements_enabled": True,
        }

        response = Wallet.update_wallet(app, payload, eth_private_key)
        self.assertTrue(response['wallet']['statements_enabled'])
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response.get('status'), 'SUCCESS')
        self.assertIsNotNone(response.get('wallet'))
        self.assertEqual(response.get('wallet').get(
            'nickname'), nickname)
        self.assertTrue(response.get('wallet').get('default'))

    def test_update_wallet_400(self):
        payload = {
            "user_handle": "",
            "nickname": ""
        }

        response = Wallet.update_wallet(app, payload, eth_private_key)
        self.assertFalse(response.get('success'))
        self.assertEqual(response.get('status_code'), 400)
        self.assertEqual(response.get('status'), 'FAILURE')

    def test_update_wallet_403(self):
        payload = {
            "user_handle": user_handle,
            "nickname": "wallet_python_updated",
            "default": True
        }

        response = Wallet.update_wallet(app, payload, '')
        self.assertFalse(response.get('success'))
        self.assertEqual(response.get('status_code'), 403)
        self.assertEqual(response.get('status'), 'FAILURE')


if __name__ == '__main__':
    unittest.main()
