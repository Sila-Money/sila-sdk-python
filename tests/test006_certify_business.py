import unittest, silasdk

from tests.test_config import *

class Test006CertifyBusinessTest(unittest.TestCase):
    def test_beneficial_owner_200(self):
        payload = {
            "user_handle": user_handle,
            "business_handle": business_handle
        }

        response = silasdk.BusinessOperations.certifyBusiness(app, payload, eth_private_key, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

if __name__ == '__main__':
    unittest.main()
