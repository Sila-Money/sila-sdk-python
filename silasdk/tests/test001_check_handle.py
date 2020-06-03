import unittest

from silasdk.tests.test_config import *
from silasdk.users import User


class Test001CheckHandleTest(unittest.TestCase):
    def test_check_handle_200(self):
        payload = {
            "user_handle": user_handle
        }
        response = User.checkHandle(app, payload)
        self.assertEqual(response["status"], "SUCCESS")

    def test_check_handle_401(self):
        payload = {
            "user_handle": ""
        }
        response = User.checkHandle(app, payload)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == "__main__":
    unittest.main()
