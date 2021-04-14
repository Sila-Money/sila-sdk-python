import unittest
import time
from silasdk.users import User
from tests.test_config import (
    app, user_handle )


class Test005CheckPartnerKycTest(unittest.TestCase):
    def test_check_partner_kyc_200(self):
        payload = {
            "query_app_handle": "digital_geko_e2e_new",
            "query_user_handle": user_handle
        }
        response = User.check_partner_kyc(app, payload)

        self.assertIsNotNone(response["status"])
        self.assertIsNotNone(response['success'])


if __name__ == '__main__':
    unittest.main()
