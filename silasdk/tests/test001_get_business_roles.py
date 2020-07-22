import unittest, silasdk

from silasdk.tests.test_config import *

class Test001GetBusinessRolesTest(unittest.TestCase):
    def test_get_business_roles(self):
        response = silasdk.BusinessInformation.getBusinessRoles(app)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["business_roles"])
        self.assertIsNotNone(response["business_roles"][0]["uuid"])
        self.assertIsNotNone(response["business_roles"][0]["name"])
        self.assertIsNotNone(response["business_roles"][0]["label"])


if __name__ == "__main__":
    unittest.main()
