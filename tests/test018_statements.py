

import unittest
import silasdk

from tests.test_config import *


class   Test018Statements(unittest.TestCase):

    def test_statements_200(self):
        payload = {
            "start_date": "2023-06-15",
            "end_date": "2023-06-15",
            "user_handle": "user_handle1_1686776339cudgjmzwckh4ohh",
            "page":1,
            "per_page":20

        }

        response = silasdk.User.statements(app, payload, eth_private_key)
        self.assertNotEquals(response['delivery_attempts'],None)
        self.assertNotEquals(response['pagination']['total_count'],0)
        
    def test_statements_400(self):
        payload = {
            "start_date": "2023-06-15",
            "end_date": "2023-06-15",
            "user_handle": "random_user",
            "page":1,
            "per_page":20

        }
    
        response = silasdk.User.statements(app, payload, eth_private_key)
        self.assertEqual(response['success'],False)
        self.assertEqual(response['status'],'FAILURE')
