

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
        app = App("sandbox", "9c17e7b767b8f4a63863caf1619ef3e9967a34b287ce58542f3eb19b5a72f076", "arc_sandbox_test_app01")
        response = silasdk.User.statements(app, payload, 'c087fb917b921f930355b97edda0ab29a5ea40963cef376be999e6aedf0efe0e')
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
        app = App("sandbox", "9c17e7b767b8f4a63863caf1619ef3e9967a34b287ce58542f3eb19b5a72f076", "arc_sandbox_test_app01")
        response = silasdk.User.statements(app, payload, 'c087fb917b921f930355b97edda0ab29a5ea40963cef376be999e6aedf0efe0e')
        self.assertEqual(response['success'],False)
        self.assertEqual(response['status'],'FAILURE')
