import uuid
import unittest
from silasdk.processingTypes import ProcessingTypes
from silasdk.transactions import Transaction
from silasdk.users import User
from tests.poll_until_status import poll
from tests.test_config import (sardine_handle, eth_private_key_6,
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

        # poll(self, response["transaction_id"], "success",
        #      app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS")
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

        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

    def test_redeem_sila_idempotency_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name": "default_plaid",
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
    
    def test_redeem_sila_200_with_card_name(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "card_name": "visa"
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key)
        
        # poll(self, response["transaction_id"], "success",
        #      app, user_handle, eth_private_key)

        self.assertTrue(response["success"])

    def test_redeem_sila_card_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "card_name": "visa",
            "processing_type": ProcessingTypes.CARD
        }
        response = Transaction.redeemSila(
            app, payload, eth_private_key)
        # poll(self, response["transaction_id"], "success",
        #      app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS")

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

    def test_redeem_sila_vaccount_200(self):
        payload = {
            "virtual_account_name": "test_v_acc",
            "user_handle": user_handle
        }
        response = User.openVirtualAccount(app, payload, eth_private_key)
        self.assertTrue(response["success"])
        v_id = response.get("virtual_account").get("virtual_account_id")

        payload = {
            "user_handle": user_handle
        }
        response = User.getPaymentMethods(app, payload, eth_private_key)

        self.assertTrue(response["success"])
        for item in response.get("payment_methods"):
            if item["payment_method_type"] == "card":
                card_id = item.get("card_id")

        descriptor = "test descriptor"
        payload = {
            "message": "issue_msg",
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_plaid",
            "descriptor": descriptor,
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH,
            "destination_id": v_id,
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)

        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        descriptor = "test descriptor"
        payload = {
            "message": "redeem_msg",
            "user_handle": user_handle,
            "amount": 100,
            "destination_id": card_id,
            "descriptor": descriptor,
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH,
            "source_id": v_id,
        }
        response = Transaction.redeemSila(app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")
        
    def test_redeem_sila_instant_settelment_200(self):
        payload = {
            "user_handle": sardine_handle,
            "amount": 50,
            "account_name": "default_plaid",
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
        }

        response = Transaction.redeemSila(
            app, payload, eth_private_key_6)
        self.assertEqual(response["status"], "SUCCESS")


    def test_redeem_wire_transection_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "account_name": "default_plaid",
            "processing_type": ProcessingTypes.WIRE,
            "business_uuid": business_uuid,
            "mock_wire_account_name": "mock_account_success"
        }
        response = Transaction.redeemSila(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "SUCCESS")
if __name__ == '__main__':
    unittest.main()
