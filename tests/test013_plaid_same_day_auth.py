import unittest, silasdk

from tests.test_config import *


class Test013PlaidSameDayAuthTest(unittest.TestCase):
    # def test_plaid_same_day_auth_200(self):
    #     payload = {
    #         "user_handle": user_handle,
    #         "account_name": "default_plaid"
    #     }
    #
    #     response = silasdk.Transaction.plaidSamedayAuth(app, payload, eth_private_key)
    #     self.assertEqual(response["status"], "SUCCESS")

    def test_plaid_same_day_auth_400(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "default"
        }

        response = silasdk.Transaction.plaidSamedayAuth(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_plaid_same_day_auth_404(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "notFound"
        }

        response = silasdk.Transaction.plaidSamedayAuth(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == '__main__':
    unittest.main()
