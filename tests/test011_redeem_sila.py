import unittest
from silasdk.processingTypes import ProcessingTypes
from silasdk.transactions import Transaction
from tests.poll_until_status import poll
from tests.test_config import (
    app, business_uuid, eth_private_key, user_handle)


class Test011RedeemSilaTest(unittest.TestCase):
    def test_redeem_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name": "default_plaid",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)

        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

    def test_redeem_sila_400(self):
        payload = {
            "user_handle": user_handle
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_redeem_sila_401(self):
        payload = {
            "user_handle": "",
            "amount": "-1"
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")
    
    def test_redeem_sila_200_with_card_name(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "card_name": "visa",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)

        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        self.assertTrue(response["success"])

    def test_redeem_sila_400_both_card_account(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name": "test_account",
            "card_name": "visa",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)

        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
