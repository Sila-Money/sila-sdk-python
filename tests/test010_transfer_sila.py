import uuid
import unittest
from silasdk.transactions import Transaction
from silasdk.users import User
from tests.poll_until_status import poll
from silasdk.processingTypes import ProcessingTypes
from tests.test_config import ( sardine_handle, eth_private_key_6,
    app, business_uuid, eth_private_key, user_handle, user_handle_2)


class Test010TransferSilaTest(unittest.TestCase):
    def test_transfer_sila_200(self):
        payload = {
            "user_handle": user_handle,
            "destination": user_handle_2,
            "amount": 100,
            "descriptor": "test descriptor",
            "business_uuid": business_uuid
        }

        response = Transaction.transferSila(
            app, payload, eth_private_key)      
        poll(self, response["transaction_id"], "success", app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

    def test_transfer_sila_idempotency_200(self):
        payload = {            
            "user_handle": user_handle,
            "destination": user_handle_2,
            "amount": 100,
            "descriptor": "test descriptor",
            "business_uuid": business_uuid,
            "transaction_idempotency_id": str(uuid.uuid4())
        }

        first_response = Transaction.transferSila(app, payload, eth_private_key)
        second_response = Transaction.transferSila(app, payload, eth_private_key)
        self.assertEqual(first_response["transaction_id"], second_response["transaction_id"])

    def test_transfer_sila_400(self):
        payload = {
            "user_handle": user_handle,
            "destination": user_handle_2,
            "crypto": "ETHS",
        }

        response = Transaction.transferSila(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_transfer_sila_401(self):
        payload = {
            "user_handle": "",
            "destination": user_handle_2,
            "crypto": "ETH",
            "amount": 1000
        }

        response = Transaction.transferSila(
            app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_transfer_sila_v2v_200(self):
        payload = {
            "virtual_account_name": "source_v_acc",
            "user_handle": user_handle
        }

        response = User.openVirtualAccount(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        source_v_id = response.get("virtual_account").get("virtual_account_id")

        payload = {
            "virtual_account_name": "destination_v_acc",
            "user_handle": user_handle
        }

        response = User.openVirtualAccount(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        destination_v_id = response.get(
            "virtual_account").get("virtual_account_id")

        descriptor = "test descriptor"
        payload = {
            "message": "issue_msg",
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_plaid",
            "descriptor": descriptor,
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH,
            "destination_id": source_v_id,
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        payload = {
            "message": "transfer_msg",
            "user_handle": user_handle,
            "source_id": source_v_id,
            "destination_id": destination_v_id,
            "destination": user_handle,
            "amount": 100,
            "descriptor": "test descriptor",
            "business_uuid": business_uuid
        }

        response = Transaction.transferSila(
            app, payload, eth_private_key)

        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])

def test_transfer_sila_v2block_chain_200(self):
        payload = {
            "virtual_account_name": "source_v_acc",
            "user_handle": user_handle
        }

        response = User.openVirtualAccount(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        source_v_id = response.get("virtual_account").get("virtual_account_id")

        payload = {
            "user_handle": user_handle
        }
        response = User.getPaymentMethods(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        for item in response.get("payment_methods"):
            if item["payment_method_type"] == "blockchain_address":
                blockchain_address = item.get("blockchain_address")

        descriptor = "test descriptor"
        payload = {
            "message": "issue_msg",
            "user_handle": user_handle,
            "amount": 200,
            "account_name": "default_plaid",
            "descriptor": descriptor,
            "business_uuid": business_uuid,
            "processing_type": ProcessingTypes.STANDARD_ACH,
            "destination_id": source_v_id,
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        payload = {
            "message": "transfer_msg",
            "user_handle": user_handle,
            "source_id": source_v_id,
            "destination_id": blockchain_address,
            "destination": user_handle,
            "amount": 100,
            "descriptor": "test descriptor",
            "business_uuid": business_uuid
        }
        
        response = Transaction.transferSila(
            app, payload, eth_private_key)

        poll(self, response["transaction_id"], "success",
             app, user_handle, eth_private_key)

        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["descriptor"], "test descriptor")
        self.assertIsNotNone(response["transaction_id"])
    

def test_transfer_sila_instant_settelment_200(self):
    payload = {
        "user_handle": sardine_handle,
        "destination": user_handle_2,
        "amount": 100,
        "descriptor": "test descriptor",
        "business_uuid": business_uuid
    }

    response = Transaction.transferSila(
        app, payload, eth_private_key_6)
    self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))

if __name__ == '__main__':
    unittest.main()
