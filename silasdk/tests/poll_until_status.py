import unittest, silasdk, time
from silasdk.tests.test_config import *

class PollUntilStatus():
    def poll(self, transactionId, expectedStatus):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                'page': 1,
                'per_page': 1,
                "transaction_id": transactionId,
            }
        }

        response = silasdk.User.getTransactions(app, payload, eth_private_key)
        status = response["transactions"][0]["status"]

        while status == "queued" or status == "pending":
            time.sleep(30)
            response = silasdk.User.getTransactions(app, payload, eth_private_key)
            status = response["transactions"][0]["status"]

        self.assertEqual(status, expectedStatus)