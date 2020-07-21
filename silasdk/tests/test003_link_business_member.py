import unittest

from silasdk.tests.test_config import *
from silasdk.businessOperations import BusinessOperations


class Test003LinkBusinessMemberTest(unittest.TestCase):
    def test_link_business_member_administrator_200(self):
        payload = {
            "user_handle": user_handle,
            "business_handle": business_handle,
            "role": "administrator",
            "details": "this is the business administrator"
        }
        response = BusinessOperations.linkBusinessMember(app, payload, eth_private_key, eth_private_key_3)
        self.assertTrue(response["success"])

    def test_link_business_member_administrator_2_200(self):
        payload = {
            "user_handle": user_handle_2,
            "business_handle": business_handle,
            "role": "administrator",
            "details": "this is the business administrator"
        }
        response = BusinessOperations.linkBusinessMember(app, payload, eth_private_key_2, eth_private_key_3)
        self.assertTrue(response["success"])


if __name__ == "__main__":
    unittest.main()
