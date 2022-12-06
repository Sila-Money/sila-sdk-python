import unittest, silasdk

from tests.test_config import *

class Test018GetStatementsData(unittest.TestCase):

    def test_get_statements_data_200(self):

        payload = {
            "user_handle": user_handle,
            "search_filters": {
                "month": "07-2022",
                "page": 1,
                "per_page": 20,
               }
        }
        response = silasdk.User.get_statements_data(app, payload, eth_private_key)
        self.assertEqual(response.get('status'), 'SUCCESS')
        self.assertEqual(response.get('status_code'), 200)
        self.assertIsNotNone(response.get("statements"))

    def test_get_statements_data_400(self):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                "month":None,
                "page": 1,
                "per_page": 20,
            }
        }
        response = silasdk.User.get_statements_data(app, payload, eth_private_key)
        self.assertFalse(response["success"])
        self.assertEqual(response.get('status_code'), 400)
