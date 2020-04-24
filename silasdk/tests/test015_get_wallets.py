import unittest

from silasdk.stellarwallet import Wallet
from silasdk.tests.test_config import *


class GetWalletsTest(unittest.TestCase):
    def test_get_wallets_200(self):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                "page": 1,
                "per_page": 20,
                "sort_ascending": False,
                "blockchain_network": "ETH",
                "blockchain_address": wallet_address,
                "nickname": "wallet_python"
            }
        }

        response = Wallet.getWallets(app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_get_wallets_400(self):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                "page": 0,
                "per_page": 20,
                "sort_ascending": False,
                "blockchain_network": "ETHS",
                "blockchain_address": wallet_address,
                "nicknames": "wallet_python"
            }
        }

        response = Wallet.getWallets(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_get_wallets_401(self):
        payload = {
            "user_handle": "",
            "search_filters": {
                "page": 1,
                "per_page": 20,
                "sort_ascending": False,
                "blockchain_network": "ETH",
                "blockchain_address": wallet_address,
                "nickname": "wallet_python"
            }
        }

        response = Wallet.getWallets(app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_get_wallets_403(self):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                "page": 1,
                "per_page": 20,
                "sort_ascending": False,
                "blockchain_network": "ETH",
                "blockchain_address": "",
                "nickname": "wallet_python"
            }
        }

        response = Wallet.getWallets(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
