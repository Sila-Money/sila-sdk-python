import uuid
import unittest
from silasdk.processingTypes import ProcessingTypes
from silasdk.transactions import Transaction
from tests.test_config import (
    app, business_uuid, eth_private_key, user_handle
)


class Test011RedeemSilaTest(unittest.TestCase):
    def test_redeem_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name": "default_mx",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name": "default_mx",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

    def test_redeem_sila_idempotency_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name": "default_mx",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH,
            "transaction_idempotency_id" : str(uuid.uuid4())
        }

        first_response = Transaction.redeemSila(app, payload, eth_private_key)
        second_response = Transaction.redeemSila(app, payload, eth_private_key)
        self.assertEqual(first_response["transaction_id"], second_response["transaction_id"])


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

    def test_redeem_sila_400_both_card_account(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name": "test_account",
            "card_name": "visa"
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)

        self.assertFalse(response["success"])


if __name__ == '__main__':
    unittest.main()
