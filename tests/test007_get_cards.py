import unittest
from silasdk.users import User
from tests.test_config import (app,eth_address, user_handle, eth_private_key)


class Test007GetCardsTest(unittest.TestCase):
    def test_001_get_cards_200(self):
        payload = {
            "user_handle": user_handle            
        }

        response = User.get_cards(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])
    
    def test_002_get_cards_400(self):
        payload = {
            "user_handle": ''            
        }

        response = User.get_cards(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == "__main__":
    unittest.main()
