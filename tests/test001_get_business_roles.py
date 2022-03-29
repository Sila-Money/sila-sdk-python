import unittest, silasdk

from tests.test_config import *

class Test001GetBusinessRolesTest(unittest.TestCase):
    def test_get_business_roles(self):
        response = silasdk.BusinessInformation.getBusinessRoles(app)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["business_roles"])
        self.assertIsNotNone(response["business_roles"][0]["uuid"])
        self.assertIsNotNone(response["business_roles"][0]["name"])
        self.assertIsNotNone(response["business_roles"][0]["label"])
        self.assertIsNotNone(response["reference"])
        self.assertIsNotNone(response["response_time_ms"])  


if __name__ == "__main__":
    unittest.main()
