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


if __name__ == '__main__':
    unittest.main()
