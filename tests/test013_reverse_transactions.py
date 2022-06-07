import unittest, requests 
import time
from silasdk.users import User
from silasdk.transactions import Transaction
from silasdk.processingTypes import ProcessingTypes
from tests.test_config import (app, user_handle, eth_address, eth_private_key)


class Test013ReverseTransactionsTest(unittest.TestCase):

    def test_001_reverse_transaction_200(self):
        payload = {
            "user_handle": user_handle,
            "amount": 200,
            "card_name": "visa"
        }

        response = Transaction.issue_sila(app, payload, eth_private_key)
        self.assertEqual(response.get("success"), True)    

        payload = {
            "user_handle": user_handle,
            "search_filters": {
                'page': 1,
                'per_page': 1,
                "transaction_id": response["transaction_id"],
            }
        }
        
        response1 = User.get_transactions(app, payload, eth_private_key) 
        while response1['transactions'][0]['status'] == "pending":
            time.sleep(50)
            response1 = User.get_transactions(app, payload, eth_private_key)     
        
        payload = {
            "user_handle": user_handle,
            "transaction_id": response["transaction_id"]
        }
        response2 = Transaction.reverseTransaction(app, payload, eth_private_key)
        self.assertTrue(response2.get('success'))

if __name__ == '__main__':
    unittest.main()
