import unittest

from silasdk.tests.test_config import *
from silasdk.businessOperations import BusinessOperations


class Test003UnlinkBusinessMemberTest(unittest.TestCase):
    def test_unlink_business_member_administrator_200(self):
        payload = {
            "user_handle": user_handle_2,
            "business_handle": business_handle,
            "role": "administrator",
        }
        response = BusinessOperations.unlinkBusinessMember(app, payload, eth_private_key_2, eth_private_key_3)
        self.assertTrue(response["success"])


if __name__ == "__main__":
    unittest.main()
