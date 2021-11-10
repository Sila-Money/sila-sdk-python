import unittest
from silasdk.users import User
from tests.test_config import (app, user_handle, eth_private_key)


class Test020GetWebhooksTest(unittest.TestCase):
    def test_001_get_webhooks_200(self):
        payload = {
            "user_handle": user_handle            
        }
        response = User.get_webhooks(app, payload, eth_private_key)
        self.assertTrue(response["success"])
    
    def test_002_get_webhooks_400(self):
        payload = {
            "user_handle": ''            
        }
        response = User.get_webhooks(app, payload, eth_private_key)
        self.assertFalse(response["success"])


if __name__ == "__main__":
    unittest.main()
