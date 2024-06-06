import unittest, silasdk

from tests.test_config import *

class Test001GetNaicsCategoriesTest(unittest.TestCase):
    def test_get_naics_categories(self):
        response = silasdk.BusinessInformation.getNaicsCategories(app)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["naics_categories"])
        self.assertEqual(response["naics_categories"]["Accommodation and Food Services"][0]["code"], 721)
        self.assertEqual(response["naics_categories"]["Accommodation and Food Services"][0]["subcategory"], "Accommodation")
        self.assertIsNotNone(response["reference"])


if __name__ == "__main__":
    unittest.main()
