import unittest
import time

from silasdk.users import User
from tests.test_config import (app, eth_private_key, user_handle)


class Test005GetEntityTest(unittest.TestCase):
    def test_get_entity_200_deprecated(self):
        payload = {
            "user_handle": user_handle
        }
        with self.assertWarns(DeprecationWarning):
            response = User.getEntity(app, payload, eth_private_key)
            self.assertTrue(response["success"])
        

    def test_get_entity_200(self):
        payload = {
            "user_handle": user_handle
        }
        response = User.get_entity(app, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["entity"])
        self.assertFalse("created" in response["entity"])

    def test_get_entity_200_with_pretty_dates(self):
        payload = {
            "user_handle": user_handle
        }
        response = User.get_entity(app, payload, eth_private_key, True)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["entity"])
        self.assertTrue("created" in response["entity"])


if __name__ == '__main__':
    unittest.main()
