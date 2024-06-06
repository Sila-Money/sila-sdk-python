import unittest
from silasdk.users import User
from silasdk.processingTypes import ProcessingTypes
from tests.test_config import (app, user_handle, sardine_handle)


class Test012GetTransactionsTest(unittest.TestCase):

    def test_get_transactions_200(self):
        lai = False
        di = False
        si = False
        dslt = False
        dlai = False

        payload = {
            "user_handle": user_handle,
            "search_filters": {
                'page': 1,
                'per_page': 13,
                'show_timelines': True
            }
        }
        response = User.get_transactions(app, payload)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])
        self.assertEqual(len(response["transactions"]), 13)
        self.assertIsNotNone(response.get('transactions')[0].get('timeline'))
        self.assertIsNotNone(response.get('transactions')[0].get('sila_ledger_type'))
        self.assertIsNotNone(response.get('transactions')[0].get('sec_code'))
        self.assertIn("provider_status",response.get("transactions")[0].keys())
        self.assertIn("provider_status",response.get("transactions")[0]["timeline"][0].keys())

        for item in response.get("transactions"):
            if item.get("ledger_account_id") and not lai:
                self.assertIsNotNone(item["ledger_account_id"])
                lai = True
            if item.get("destination_id") and not di:
                self.assertIsNotNone(item["destination_id"])
                di = True
            if item.get("source_id") and not si:
                self.assertIsNotNone(item["source_id"])
                si = True
            if item.get("destination_sila_ledger_type") and not dslt:
                self.assertIsNotNone(item["destination_sila_ledger_type"])
                dslt = True
            if item.get("destination_ledger_account_id") and not dlai:
                self.assertIsNotNone(item["destination_ledger_account_id"])
                dlai = True
        self.assertTrue(lai)
        self.assertTrue(di)
        self.assertTrue(si)
        self.assertTrue(dslt)
        self.assertTrue(dlai)

    def test_get_transactions_without_user_handle_200(self):
        response = User.get_transactions(app)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

    def test_get_transactions_200_with_error_code(self):
        payload = {
            "user_handle": user_handle,
            "search_filters": {
                'page': 1,
                'per_page': 1,
                'show_timelines': True,
                'min_sila_amount': 410,
                'max_sila_amount': 430
            }
        }
        response = User.get_transactions(app, payload)
        
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])
        self.assertEqual(len(response["transactions"]), 1)
        self.assertIsNotNone(response.get('transactions')[0].get('return_code'))
        self.assertIsNotNone(response.get('transactions')[0].get('return_desc'))

    def test_get_transactions_200_with_filters(self):
        payload = {
            'user_handle': user_handle,
            'search_filters': {
                'statuses': ['success'],
                'transaction_types': ['issue']
            }
        }
        response = User.get_transactions(app, payload)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])
        self.assertGreater(len(response.get('transactions')), 1)
        self.assertEqual(response.get('transactions')
                         [0].get('status'), 'success')
        self.assertEqual(response.get('transactions')[
                         0].get('transaction_type'), 'issue')

        payment_method_id = response.get("transactions")[0].get("transaction_id")
        payload = {
            'user_handle': user_handle,
            'search_filters': {
                'payment_method_id': payment_method_id
            }
        }
        response = User.get_transactions(app, payload)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

    def test_get_transactions_400(self):
        payload = {
            "user_handle": ""
        }

        response = User.get_transactions(app, payload)
        self.assertFalse(response.get('success'))
        self.assertEqual(response.get('status_code'), 400)

    def test_get_transactions_filter_by_account_name(self):
        payload = {
            "user_handle": user_handle,
            'search_filters': {
                'bank_account_name': 'default'
            }
        }
        response = User.get_transactions(app, payload)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

    def test_get_instant_settlement_transactions_200(self):
        payload = {
            'user_handle': sardine_handle,
            'search_filters': {
                'processing_type': ProcessingTypes.INSTANT_SETTLEMENT,
            }
        }
        response = User.get_transactions(app, payload)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))


if __name__ == '__main__':
    unittest.main()
