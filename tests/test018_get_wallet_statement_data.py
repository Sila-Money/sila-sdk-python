import unittest, silasdk

from tests.test_config import *

class Test018GetWalletStatementData(unittest.TestCase):
    def test_get_wallet_statement_data_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = silasdk.Wallet.getWallet(app, payload, eth_private_key)
        wallet_id = response.get("wallet").get("wallet_id")
        payload = {
            "wallet_id":wallet_id,
            "search_filters": {
                "start_month": "07-2022",
                "end_month": "11-2022",
                "page": 1,
                "per_page": 100
            }
        }
        response = silasdk.User.get_wallet_statement_data(app, payload, eth_private_key)
        self.assertEqual(response.get('status'), 'SUCCESS')
        self.assertEqual(response.get('status_code'), 200)
        self.assertIsNotNone(response.get("statements"))


    def test_get_wallet_statement_data_400(self):

        payload = {
            "user_handle": user_handle,
            "wallet_id":None,
            "search_filters": {
                "start_month": "07-2022",
                "end_month": "11-2022",
                "page": 1,
                "per_page": 100
            }
        }
        response = silasdk.User.get_wallet_statement_data(app, payload, eth_private_key)
        self.assertFalse(response["success"])
        self.assertEqual(response.get('status_code'), 400)
