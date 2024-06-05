import unittest, requests 
from silasdk.users import User
from tests.test_config import (app, user_handle, eth_private_key, user_handle_2, eth_private_key_2, plaid_token_for_card_url, plaid_token_for_card_payload, plaid_token_for_card_headers)


class Test008DeleteCardTest(unittest.TestCase):
    def test_001_link_card_200(self):
        """Generate plaid legacy token"""

        url = plaid_token_for_card_url
        payload = plaid_token_for_card_payload
        headers = plaid_token_for_card_headers
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.text
        card_token = response[3:]
        payload = {
            "user_handle": user_handle,
            "card_name": "unlink",
            "account_postal_code": "12345",
            "token": card_token
        }

        response = User.link_card(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

    def test_002_delete_card_200(self):
        payload = {
            "user_handle": user_handle_2,
            "card_name": "visaas",
            "provider" : "CKO"            
        }

        response = User.delete_card(app, payload, eth_private_key_2)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

    def test_003_delete_card_400(self):
        payload = {
            "user_handle": '',
            "card_name": "unlink",           
        }

        response = User.delete_card(app, payload, eth_private_key)
        self.assertFalse(response["success"])  



if __name__ == "__main__":
    unittest.main()
