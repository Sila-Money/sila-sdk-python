import unittest, silasdk

from tests.test_config import *

class Test003CheckHandleFailTest(unittest.TestCase):
    def test_check_handle_failure_200(self):
        payload = {
            "user_handle": user_handle
        }
        response = silasdk.User.checkHandle(app, payload)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == "__main__":
    unittest.main()
