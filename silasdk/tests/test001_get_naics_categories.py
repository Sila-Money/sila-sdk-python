import unittest

from silasdk.tests.test_config import *
from silasdk.businessInformation import *

class Test001GetNaicsCategoriesTest(unittest.TestCase):
    def test_get_naics_categories(self):
        response = BusinessInformation.getNaicsCategories(app)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["naics_categories"])
        self.assertEqual(response["naics_categories"]["Accommodation and Food Services"][0]["code"], 721)
        self.assertEqual(response["naics_categories"]["Accommodation and Food Services"][0]["subcategory"], "Accommodation")


if __name__ == "__main__":
    unittest.main()
