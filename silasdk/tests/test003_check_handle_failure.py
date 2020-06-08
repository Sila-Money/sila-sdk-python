import unittest

from silasdk.tests.test_config import *
from silasdk.users import User


class Test003CheckHandleFailTest(unittest.TestCase):
    def test_check_handle_failure_200(self):
        payload = {
            "user_handle": user_handle
        }
        response = User.checkHandle(app, payload)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == "__main__":
    unittest.main()
