import unittest, time

from silasdk.users import User
from silasdk.tests.test_config import *


class Test005CheckKycTest(unittest.TestCase):
    def test_check_kyc_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = User.checkKyc(app, payload, eth_private_key)
        response_2 = User.checkKyc(app, payload, eth_private_key_2)
        while response["status"] != "SUCCESS" or response_2["status"] != "SUCCESS":
            time.sleep(100)
            response = User.checkKyc(app, payload, eth_private_key)
            response_2 = User.checkKyc(app, payload, eth_private_key_2)

        self.assertEqual(response["status"], "SUCCESS")


if __name__ == '__main__':
    unittest.main()
