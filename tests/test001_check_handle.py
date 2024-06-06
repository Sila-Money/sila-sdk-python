import unittest
import silasdk

from tests.test_config import (user_handle, app)


class Test001CheckHandleTest(unittest.TestCase):
    def test_check_handle_200(self):
        payload = {
            "user_handle": user_handle
        }
        response = silasdk.User.checkHandle(app, payload)
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))

    def test_check_handle_401(self):
        payload = {
            "user_handle": ""
        }
        response = silasdk.User.checkHandle(app, payload)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == "__main__":
    unittest.main()
