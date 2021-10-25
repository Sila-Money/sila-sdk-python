import unittest, requests 
from silasdk.users import User
from tests.test_config import (app,eth_address, user_handle, eth_private_key)


class Test008DeleteCardTest(unittest.TestCase):
    def test_001_link_card_200(self):
        """Generate plaid legacy token"""

        url = "https://sso.sandbox.tabapay.com:8443/v2/SSOEncrypt"
        payload = "cBm0RU8eASGfSxLYJjsG73Q\tn5403879999999997\te202205\ts2545"
        headers = {
            'Content-Type': 'application/tabapay-compact'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.text
        card_token = response[3:]
        
        payload = {
            "user_handle": user_handle,
            "card_name":"unlink",
            "account_postal_code":"12345",
            "token":card_token
        }

        response = User.link_card(app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_002_delete_card_200(self):
        payload = {
            "user_handle": user_handle,
            "card_name":"unlink"            
        }

        response = User.delete_card(app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_003_delete_card_400(self):
        payload = {
            "user_handle": '',
            "card_name":"unlink"            
        }

        response = User.delete_card(app, payload, eth_private_key)
        self.assertFalse(response["success"])  



if __name__ == "__main__":
    unittest.main()