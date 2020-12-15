import unittest, silasdk

from tests.test_config import *

class Test002GetEntitiesTest(unittest.TestCase):
    def test_get_entities_businesses_200(self):
        payload = {
            "entity_type": "business"
        }

        response = silasdk.User.getEntities(app, payload)
        self.assertTrue(response["success"])
        self.assertFalse(response["entities"]["individuals"])

    def test_get_entities_individuals_200(self):
        payload = {
            "entity_type": "individual"
        }

        response = silasdk.User.getEntities(app, payload)
        self.assertTrue(response["success"])
        self.assertFalse(response["entities"]["businesses"])

    def test_get_entities_pagination_200(self):
        payload = {}

        response = silasdk.User.getEntities(app, payload, 3, 1)
        self.assertTrue(response["success"])
        self.assertEqual(response["pagination"]["returned_count"], 3)
        self.assertEqual(response["pagination"]["current_page"], 1)


if __name__ == "__main__":
    unittest.main()
