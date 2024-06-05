import unittest, silasdk

from tests.test_config import *

class Test001GetInstitutionsTest(unittest.TestCase):
    def test_get_institutions(self):
        payload = {
            "institution_name": "1st advantage bank"
        }
        response = silasdk.User.get_institutions(app, payload)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])
        self.assertIsNotNone(response["response_time_ms"])  


if __name__ == "__main__":
    unittest.main()
