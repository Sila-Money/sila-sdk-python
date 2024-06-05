import unittest, silasdk

from tests.test_config import *

class Test002GetEntitiesTest(unittest.TestCase):
    def test_get_entities_businesses_200(self):
        payload = {
            "entity_type": "business"
        }

        response = silasdk.User.getEntities(app, payload)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertFalse(response["entities"]["individuals"])
        self.assertIsNotNone(response["reference"])

    def test_get_entities_individuals_200(self):
        payload = {
            "entity_type": "individual"
        }

        response = silasdk.User.getEntities(app, payload)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertFalse(response["entities"]["businesses"])
        self.assertIsNotNone(response["reference"])

    def test_get_entities_pagination_200(self):
        payload = {}

        response = silasdk.User.getEntities(app, payload, 3, 1)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response["pagination"]["returned_count"], 3)
        self.assertEqual(response["pagination"]["current_page"], 1)
        self.assertIsNotNone(response["reference"])


if __name__ == "__main__":
    unittest.main()
