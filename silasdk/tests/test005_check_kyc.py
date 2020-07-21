import unittest
import time

from silasdk.users import User
from silasdk.tests.test_config import *


class Test005CheckKycTest(unittest.TestCase):
    def test_check_kyc_200(self):
        payload = {
            "user_handle": user_handle
        }
        response = User.checkKyc(app, payload, eth_private_key)

        payload = {
            "user_handle": user_handle_2
        }
        response_2 = User.checkKyc(app, payload, eth_private_key_2)

        payload = {
            "user_handle": business_handle
        }
        response_3 = User.checkKyc(app, payload, eth_private_key_3)
        while response["status"] != "SUCCESS" or response_2["status"] != "SUCCESS" or "Business has passed verification" not in response_3["message"]:
            time.sleep(100)
            payload = {
                "user_handle": user_handle
            }
            response = User.checkKyc(app, payload, eth_private_key)

            payload = {
                "user_handle": user_handle_2
            }
            response_2 = User.checkKyc(app, payload, eth_private_key_2)

            payload = {
                "user_handle": business_handle
            }
            response_3 = User.checkKyc(app, payload, eth_private_key_3)

        self.assertEqual(response["status"], "SUCCESS")


if __name__ == '__main__':
    unittest.main()
