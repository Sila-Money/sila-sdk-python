import unittest, silasdk
from tests.test_config import *


class Test006CertifyBeneficialOwnerTest(unittest.TestCase):
    def test_beneficial_owner_200(self):
        payload = {
            "user_handle": user_handle_2
        }

        entity = silasdk.User.getEntity(app, payload, eth_private_key_2)

        payload = {
            "user_handle": user_handle,
            "business_handle": business_handle,
            "member_handle": user_handle_2,
            "certification_token": entity["memberships"][0]["certification_token"]
        }

        response = silasdk.BusinessOperations.certifyBeneficialOwner(app, payload, eth_private_key, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

if __name__ == '__main__':
    unittest.main()
