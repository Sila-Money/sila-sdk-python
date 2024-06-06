import unittest
from silasdk.businessOperations import BusinessOperations
from tests.test_config import (
    app, business_handle, eth_private_key, eth_private_key_2, eth_private_key_3, user_handle, user_handle_2)


class Test003LinkBusinessMemberTest(unittest.TestCase):
    def test_link_business_member_administrator_200(self):
        payload = {
            "user_handle": user_handle,
            "business_handle": business_handle,
            "role": "administrator",
            "details": "this is the business administrator"
        }
        response = BusinessOperations.linkBusinessMember(
            app, payload, eth_private_key, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

    def test_link_business_member_controlling_officer_200(self):
        payload = {
            "user_handle": user_handle,
            "business_handle": business_handle,
            "role": "controlling_officer",
            "details": "this is the controlling officer"
        }
        response = BusinessOperations.linkBusinessMember(
            app, payload, eth_private_key, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

    def test_link_business_member_administrator_2_200(self):
        payload = {
            "user_handle": user_handle_2,
            "business_handle": business_handle,
            "role": "administrator",
            "details": "this is the business administrator"
        }
        response = BusinessOperations.linkBusinessMember(
            app, payload, eth_private_key_2, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

    def test_link_business_member_beneficial_owner_200(self):
        payload = {
            "user_handle": user_handle_2,
            "business_handle": business_handle,
            "role": "beneficial_owner",
            "details": "this is the beneficial owner",
            "ownership_stake": 0.66
        }
        response = BusinessOperations.linkBusinessMember(
            app, payload, eth_private_key_2, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])


if __name__ == "__main__":
    unittest.main()
