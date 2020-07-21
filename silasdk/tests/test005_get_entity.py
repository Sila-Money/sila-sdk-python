import unittest, time

from silasdk.users import User
from silasdk.tests.test_config import *


class Test005GetEntityTest(unittest.TestCase):
    def test_get_entity_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = User.getEntity(app, payload, eth_private_key)
        self.assertTrue(response["success"])


if __name__ == '__main__':
    unittest.main()
