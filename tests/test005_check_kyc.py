import unittest
import time
from silasdk.users import User
from tests.test_config import (app, business_handle, eth_private_key, eth_private_key_2,
                               eth_private_key_3, user_handle, user_handle_2, sardine_handle, eth_private_key_6)


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

        payload = {
            "user_handle": sardine_handle,
            "kyc_level": "INSTANT-ACHV2"
        }
        response_4 = User.checkKyc(app, payload, eth_private_key_6)
        # while response["status"] != "SUCCESS" or response_2["status"] != "SUCCESS" or \
        #       response_4["status"] != "SUCCESS" or "Business has passed verification" not in response_3["message"]:
        #     time.sleep(100)
        #     payload = {
        #         "user_handle": user_handle
        #     }
        #     response = User.checkKyc(app, payload, eth_private_key)

        #     payload = {
        #         "user_handle": user_handle_2
        #     }
        #     response_2 = User.checkKyc(app, payload, eth_private_key_2)

        #     payload = {
        #         "user_handle": business_handle
        #     }
        #     response_3 = User.checkKyc(app, payload, eth_private_key_3)

        #     payload = {
        #         "user_handle": sardine_handle,
        #         "kyc_level": "INSTANT-ACHV2"
        #     }
        #     response_4 = User.checkKyc(app, payload, eth_private_key_6)
        # self.assertEqual(response["status"], "SUCCESS")


if __name__ == '__main__':
    unittest.main()
