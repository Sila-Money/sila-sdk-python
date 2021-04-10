import unittest

from silasdk.users import User
from tests.test_config import *

class Test006PlaidUpdateLinkTokenTest(unittest.TestCase):
    def test_plaid_update_link_token_200(self):
        payload = {
            'user_handle': user_handle,
            'account_name': 'default_plaid'
        }
        response = User.plaid_update_link_token(app, payload)
        
        self.assertTrue(response["success"])
        self.assertIsNotNone(response['link_token'])
        self.assertIsNotNone(response['status'])
        self.assertIsNotNone(response['message'])

if __name__ == '__main__':
    unittest.main()
