

import unittest
import silasdk

from tests.test_config import *


class   Test018ResendStatements(unittest.TestCase):

    def test_resend_statements_200(self):
        payload = {
           "email": "sunilarc14@silamoney.com",
           "statement_id" : "59a4feba-0fcd-40ac-bd9a-59e47da0b640"
        }
        
        app = App("sandbox", "9c17e7b767b8f4a63863caf1619ef3e9967a34b287ce58542f3eb19b5a72f076", "arc_sandbox_test_app01")
        response = silasdk.User.resend_statements(app, payload, eth_private_key)
        self.assertTrue(response['success'])
        self.assertEqual(response['status'],"SUCCESS")

    def test_resend_statements_400(self):
        payload = {
           "statement_id" : "59a4feba-0fcd-40ac-bd9a-59e47da0b640"
        }
        
        app = App("sandbox", "9c17e7b767b8f4a63863caf1619ef3e9967a34b287ce58542f3eb19b5a72f076", "arc_sandbox_test_app01")
        response = silasdk.User.resend_statements(app, payload, eth_private_key)
        self.assertFalse(response['success'])
        self.assertEqual(response['status'],"FAILURE")
