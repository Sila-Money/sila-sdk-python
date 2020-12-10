import unittest, silasdk

from tests.test_config import *

class Test006LinkAccountTest(unittest.TestCase):
    def test_link_account_200(self):
        options = {
            "public_key": "fa9dd19eb40982275785b09760ab79",
            "initial_products": ["transactions"],
            "institution_id": "ins_109508",
            "credentials": {
                "username": "user_good",
                "password": "pass_good"
            }
        }

        plaid_response = app.postPlaid("https://sandbox.plaid.com/link/item/create", options)
        payload = {
            "user_handle": user_handle,
            "account_name": "default",
            "account_number": "123456789012",
            "routing_number": "123456789",
            "account_type": "CHECKING",
        }

        response = silasdk.User.linkAccount(app, payload, eth_private_key, False)
        self.assertEqual(response["status"], "SUCCESS")

    def test_link_account_plaid_200(self):
        options = {
            "public_key": "fa9dd19eb40982275785b09760ab79",
            "initial_products": ["transactions"],
            "institution_id": "ins_109508",
            "credentials": {
                "username": "user_good",
                "password": "pass_good"
            }
        }

        plaid_response = app.postPlaid("https://sandbox.plaid.com/link/item/create", options)
        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid",
            "public_token": plaid_response["public_token"],
            "selected_account_id": plaid_response["accounts"][0]["account_id"],
            "message": "link_account_msg"
        }

        response = silasdk.User.linkAccount(app, payload, eth_private_key, True)
        self.assertEqual(response["status"], "SUCCESS")

    def test_link_account_400(self):
        options = {
            "public_key": "fa9dd19eb40982275785b09760ab79",
            "initial_products": ["transactions"],
            "institution_id": "ins_109508",
            "credentials": {
                "username": "user_good",
                "password": "pass_good"
            }
        }

        plaid_response = app.postPlaid("https://sandbox.plaid.com/link/item/create", options)
        payload = {
            "account_name": "default",
            "public_token": "",
            "selected_account_id": plaid_response["accounts"][0]["account_id"]
        }

        response = silasdk.User.linkAccount(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == '__main__':
    unittest.main()
