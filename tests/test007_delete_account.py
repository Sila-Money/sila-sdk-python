import unittest

from silasdk.users import User
from tests.test_config import (
    app, eth_private_key, user_handle)


class Test007DeleteAccountTest(unittest.TestCase):
    def test_delete_account_200(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "unlink"
        }

        response = User.delete_account(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["account_name"], "unlink")
        self.assertIsNotNone(response["reference"])

if __name__ == '__main__':
    unittest.main()
