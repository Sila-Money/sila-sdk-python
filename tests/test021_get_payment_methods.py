import unittest
import silasdk

from tests.test_config import *


class Test021GetPaymentMethods(unittest.TestCase):
    def test_get_payment_methods_200(self):
        payload = {
            "user_handle": user_handle
        }
        response = silasdk.User.getPaymentMethods(
            app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        for method in response["payment_methods"]:
            if method["payment_method_type"] == "virtual_account":
                self.assertEqual(method["payment_method_type"], "virtual_account")
                self.assertIsNotNone(method["ach_credit_enabled"])
                self.assertIsNotNone(method["ach_debit_enabled"])


if __name__ == '__main__':
    unittest.main()
