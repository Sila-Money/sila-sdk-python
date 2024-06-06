import time
import unittest
from silasdk.users import User
from tests.test_config import (
    app,
    business_handle,
    eth_private_key,
    eth_private_key_2,
    eth_private_key_3,
    user_handle,
    user_handle_2,
    sardine_handle,
    eth_private_key_6
)


class Test005CheckKycTest(unittest.TestCase):

    def check_kyc_status(self, app, payloads, eth_private_keys, timeout=100):
        verification_statuses = {payload["user_handle"]: None for payload in payloads}
        start_time = time.time()

        # Initial sleep of 20 seconds
        time.sleep(20)

        # Loop until all handles have verification_status or timeout
        while not all(status is not None for status in verification_statuses.values()):
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= timeout:
                print("Timeout reached. Giving up.")
                break

            for payload, key in zip(payloads, eth_private_keys):
                user_handle = payload["user_handle"]
                if verification_statuses[user_handle] is None:
                    response = User.checkKyc(app, payload, key)
                    if response.get('verification_status') is not None:
                        verification_statuses[user_handle] = response

            # Sleep for 5 seconds before checking again
            time.sleep(5)

        return verification_statuses

    def test_check_kyc_200(self):
        payloads = [
            {"user_handle": user_handle},
            {"user_handle": user_handle_2},
            {"user_handle": business_handle},
            {"user_handle": sardine_handle, "kyc_level": "INSTANT-ACHV2"}
        ]

        eth_private_keys = [eth_private_key, eth_private_key_2, eth_private_key_3, eth_private_key_6]

        responses = self.check_kyc_status(app, payloads, eth_private_keys)

        response = responses[user_handle]
        response_2 = responses[user_handle_2]
        response_3 = responses[business_handle]
        response_4 = responses[sardine_handle]

        self.assertIn(user_handle, response["message"])
        self.assertIsNotNone(response['verification_status'])
        self.assertIsNotNone(response['verification_history'])

        self.assertIn(user_handle_2, response_2["message"])
        self.assertIsNotNone(response_2['verification_status'])
        self.assertIsNotNone(response_2['verification_history'])

        self.assertIn("Business has passed verification", response_3["message"])
        self.assertIsNotNone(response_3['verification_status'])
        self.assertIsNotNone(response_3['verification_history'])

        self.assertIn(sardine_handle, response_4["message"])
        self.assertIsNotNone(response_4['verification_status'])
        self.assertIsNotNone(response_4['verification_history'])


if __name__ == '__main__':
    unittest.main()
