import unittest, silasdk

from tests.test_config import *

class Test003UnlinkBusinessMemberTest(unittest.TestCase):
    def test_unlink_business_member_administrator_200(self):
        payload = {
            "user_handle": user_handle_2,
            "business_handle": business_handle,
            "role": "administrator",
        }
        response = silasdk.BusinessOperations.unlinkBusinessMember(app, payload, eth_private_key_2, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])


if __name__ == "__main__":
    unittest.main()
