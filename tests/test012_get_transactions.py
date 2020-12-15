import unittest
from silasdk.users import User
from silasdk.processingTypes import ProcessingTypes
from tests.test_config import (app, eth_private_key, user_handle)


class Test012GetTransactionsTest(unittest.TestCase):
    def test_get_transactions_200_deprecated(self):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                'page': 1,
                'per_page': 1
            }
        }
        with self.assertWarns(DeprecationWarning):
            response = User.getTransactions(app, payload, eth_private_key)
            self.assertTrue(response["success"])
            self.assertEqual(len(response["transactions"]), 1)
            self.assertEqual(
                response["transactions"][0]["processing_type"], ProcessingTypes.STANDARD_ACH)

    def test_get_transactions_200(self):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                'page': 1,
                'per_page': 1,
                'show_timelines': True
            }
        }
        response = User.get_transactions(app, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertEqual(len(response["transactions"]), 1)
        self.assertEqual(
            response["transactions"][0]["processing_type"], ProcessingTypes.STANDARD_ACH)
        self.assertIsNotNone(response.get('transactions')[0].get('timeline'))

    def test_get_transactions_200_with_filters(self):
        payload = {
            'user_handle': user_handle,
            'search_filters': {
                'statuses': ['success'],
                'transaction_types': ['issue']
            }
        }
        response = User.get_transactions(app, payload, eth_private_key)

        self.assertTrue(response.get('success'))
        self.assertGreater(len(response.get('transactions')), 1)
        self.assertEqual(response.get('transactions')
                         [0].get('status'), 'success')
        self.assertEqual(response.get('transactions')[
                         0].get('transaction_type'), 'issue')

    def test_get_transactions_400(self):
        payload = {
            "user_handle": ""
        }

        response = User.get_transactions(app, payload, eth_private_key)
        self.assertFalse(response.get('success'))
        self.assertEqual(response.get('status_code'), 400)


if __name__ == '__main__':
    unittest.main()
