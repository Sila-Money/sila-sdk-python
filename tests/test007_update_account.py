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

        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["account"]["account_name"], "accountupdated")

if __name__ == '__main__':
    unittest.main()
