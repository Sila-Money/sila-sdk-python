import unittest, silasdk

from tests.test_config import *

class Test001GetBusinessTypesTest(unittest.TestCase):
    def test_get_business_types(self):
        response = silasdk.BusinessInformation.getBusinessTypes(app)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["business_types"])
        self.assertIsNotNone(response["business_types"][0]["uuid"])
        self.assertIsNotNone(response["business_types"][0]["name"])
        self.assertIsNotNone(response["business_types"][0]["label"])
        self.assertIsNotNone(response["reference"])


if __name__ == "__main__":
    unittest.main()
