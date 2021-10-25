import unittest

from silasdk.processingTypes import ProcessingTypes
from silasdk.transactions import Transaction
from tests.poll_until_status import poll
from tests.test_config import (
    app, business_uuid, instant_ach_handle, user_handle, eth_private_key, eth_private_key_4)


class Test009IssueSilaTest(unittest.TestCase):

    def test_issue_sila_200_deprecated(self):
        descriptor = "test descriptor"
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_plaid",
            "descriptor": descriptor,
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH
        }

        with self.assertWarns(DeprecationWarning):
            response = Transaction.issueSila(app, payload, eth_private_key)
            self.assertEqual(response.get("success"), True)

            poll(self, response["transaction_id"], "success",
                 app, user_handle, eth_private_key)

            self.assertEqual(response["status"], "SUCCESS")
            self.assertEqual(response["descriptor"], descriptor)
            self.assertIsNotNone(response["transaction_id"])

    def test_issue_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_plaid"
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(response.get("success"), True)

        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS")
        self.assertIsNotNone(response["transaction_id"])

        payload = {
            "user_handle": user_handle,
            "amount": 420,
            "account_name": "default_plaid"
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(response.get("success"), True)

    def test_issue_sila_400(self):
        payload = {
            "user_handle": user_handle,
            "amount": "-1"
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_issue_sila_200_with_card_name(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "card_name": "visa"
        }
        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertTrue(response["success"])   
    
    def test_issue_sila_400_card_name_account(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "test_account",
            "card_name": "visa"
        }
        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertFalse(response["success"])         

if __name__ == '__main__':
    unittest.main()
