import unittest

from silasdk.tests.test_config import *
from silasdk.businessInformation import *

class Test001GetBusinessTypesTest(unittest.TestCase):
    def test_get_business_types(self):
        response = BusinessInformation.getBusinessTypes(app)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["business_types"])
        self.assertIsNotNone(response["business_types"][0]["uuid"])
        self.assertIsNotNone(response["business_types"][0]["name"])
        self.assertIsNotNone(response["business_types"][0]["label"])


if __name__ == "__main__":
    unittest.main()
