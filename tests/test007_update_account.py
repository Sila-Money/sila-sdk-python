import unittest

from silasdk.users import User
from tests.test_config import (
    app, eth_private_key, user_handle)


class Test007UpdateAccountTest(unittest.TestCase):
    def test_update_account_200(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "forupdate",
            "new_account_name": "accountupdated"
        }

        response = User.update_account(
            app, payload, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["account"]["account_name"], "accountupdated")
        self.assertIsNotNone(response["account"]['web_debit_verified'])

    def test_freeze_account(self):
        """Verify user is able to freeze there bank account."""
        payload = {
            "user_handle": user_handle,
            "account_name": "forupdate",
            "active": False
        }
        response = User.update_account(
            app, payload, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["account"]["active"], False)
        self.assertEqual(response["account"]["account_status"], 'inactive')

    def test_unfreeze_account(self):
        """Verify user is able to unfreeze the freeze account"""
        bank_name = "unfreeze_account"
        payload = {
            "user_handle": user_handle,
            "account_name": "forupdate",
            "active": True
        }
        response = User.update_account(
            app, payload, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["account"]["active"], True)
        self.assertEqual(response["account"]["account_status"], 'active')

if __name__ == '__main__':
    unittest.main()
