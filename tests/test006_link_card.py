import unittest, requests 
from silasdk.users import User
from tests.test_config import (app, user_handle, eth_private_key, plaid_token_for_card_url, plaid_token_for_card_payload, plaid_token_for_card_headers)


class Test006LinkCardTest(unittest.TestCase):
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
            "card_name": "visa",
            "account_postal_code": "12345",
            "token": card_token
        }

        response = User.link_card(app, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["reference"])


if __name__ == "__main__":
    unittest.main()
