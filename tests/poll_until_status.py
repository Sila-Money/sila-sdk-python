from unittest import TestCase
from silasdk.client import App
from silasdk.users import User
import time


def poll(test: TestCase, transaction_id: str, expected_status: str, app: App, user_handle: str, eth_private_key: str):
    payload = {
        "user_handle": user_handle,
        "search_filters": {
            'page': 1,
            'per_page': 1,
            "transaction_id": transaction_id,
        }
    }

    response = User.get_transactions(app, payload, eth_private_key)
    status = response["transactions"][0]["status"]

    time.sleep(30)

    while status == "queued" or status == "pending":
        time.sleep(5)
        response = User.get_transactions(
            app, payload, eth_private_key)
        status = response["transactions"][0]["status"]

    test.assertEqual(status, expected_status)
