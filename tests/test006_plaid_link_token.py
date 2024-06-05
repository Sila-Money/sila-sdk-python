import unittest

from silasdk.users import User
from tests.test_config import *

class Test006PlaidLinkTokenTest(unittest.TestCase):
    def test_plaid_link_token_200(self):
        response = User.plaid_link_token(app, user_handle, android_package_name)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response['link_token'])
        self.assertIsNotNone(response["reference"])

if __name__ == '__main__':
    unittest.main()
