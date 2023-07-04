
import unittest
import silasdk

from tests.test_config import *


class Test005Virtual_account(unittest.TestCase):

    def test_open_virtual_account_200(self):
        payload = {
            "virtual_account_name": "test_v_acc",
            "user_handle": user_handle,
            "ach_credit_enabled": True,
            "ach_debit_enabled": False,
            "statements_enabled": True
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertTrue(response["virtual_account"]["statements_enabled"])
        self.assertIsNotNone(response.get('virtual_account').get('ach_debit_enabled'))
        self.assertIsNotNone(response.get('virtual_account').get('ach_credit_enabled'))
        
    def test_open_virtual_account_400(self):
        payload = {
            "virtual_account_name": "test_v_acc"
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_update_virtual_account_200(self):
        payload = {
            "user_handle": user_handle,
            "virtual_account_name": "test_update_v_acc",
            "ach_credit_enabled": True,
            "ach_debit_enabled": False
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        v_id = response.get("virtual_account").get("virtual_account_id")

        payload = {
            "user_handle": user_handle,
            "virtual_account_id": v_id,
            "virtual_account_name": "updates_test_v_acc",
            "active": False,
            "ach_debit_enabled": True,
            "ach_credit_enabled": False,
            "statements_enabled": True,
        }

        response = silasdk.User.updateVirtualAccount(
            app, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertTrue(response["virtual_account"]["statements_enabled"])
        self.assertTrue(response.get('virtual_account').get('ach_debit_enabled'))
        self.assertFalse(response.get('virtual_account').get('ach_credit_enabled'))

    def test_zget_virtial_accounts_200(self):
        payload = {
            "user_handle": user_handle,
        }

        response = silasdk.User.getVirtualAccounts(
            app, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response.get('virtual_accounts')[0].get('ach_debit_enabled'))
        self.assertIsNotNone(response.get('virtual_accounts')[0].get('ach_credit_enabled'))

    def test_zget_virtial_account_200(self):
        payload = {
            "user_handle": user_handle,
            "virtual_account_name": "test_get_v_acc"
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        v_id = response.get("virtual_account").get("virtual_account_id")

        payload = {
            "user_handle": user_handle,
            "virtual_account_id": v_id,
        }

        response = silasdk.User.getVirtualAccount(
            app, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response.get('virtual_account').get('ach_debit_enabled'))
        self.assertIsNotNone(response.get('virtual_account').get('ach_credit_enabled'))
        

    def test_close_virtual_account_200(self):
        payload = {
            "user_handle": user_handle,
            "virtual_account_name": "test_close_v_acc"
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        v_id = response.get("virtual_account").get("virtual_account_id")
        v_no = response.get("virtual_account").get("account_number")

        payload = {
            "user_handle": user_handle,
            "virtual_account_id": v_id,
            "account_number": v_no
        }

        response = silasdk.User.closeVirtualAccount(
            app, payload, eth_private_key)
        self.assertTrue(response["virtual_account"]["statements_enabled"])
        self.assertTrue(response["success"])

    def test_create_virtual_account_ach_transaction_200(self):
        payload = {
            "user_handle": user_handle,
            "virtual_account_name": "test_close_v_acc"
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        v_no = response.get("virtual_account").get("account_number")

        payload = {
            "user_handle": user_handle,
            "amount": 50,
            "virtual_account_number": v_no,
            "tran_code": 22,
            "entity_name": "Test transfer",
        }

        response = silasdk.User.testVirtualAaccountAchTransaction(
            app, payload, eth_private_key)
        self.assertTrue(response["success"])

if __name__ == "__main__":
    unittest.main()
