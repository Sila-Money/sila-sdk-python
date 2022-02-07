
import unittest
import silasdk

from tests.test_config import *


class Test005Virtual_account(unittest.TestCase):

    def test_open_virtual_account_200(self):
        payload = {
            "virtual_account_name": "test_v_acc",
            "user_handle": user_handle
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        self.assertTrue(response["success"])

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
            "virtual_account_name": "test_update_v_acc"
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        v_id = response.get("virtual_account").get("virtual_account_id")

        payload = {
            "user_handle": user_handle,
            "virtual_account_id": v_id,
            "virtual_account_name": "updates_test_v_acc",
            "active": False
        }

        response = silasdk.User.updateVirtualAccount(
            app, payload, eth_private_key)
        self.assertTrue(response["success"])

    def test_update_virtual_account_400(self):
        payload = {
            "user_handle": user_handle,
            "virtual_account_name": "test_update_v_acc"
        }
        response = silasdk.User.openVirtualAccount(
            app, payload, eth_private_key)
        v_id = response.get("virtual_account").get("virtual_account_id")

        payload = {
            "user_handle": user_handle,
            "virtual_account_id": v_id,
            "active": True
        }

        response = silasdk.User.updateVirtualAccount(
            app, payload, eth_private_key)
        self.assertFalse(response["success"])

    def test_zget_virtial_accounts_200(self):
        payload = {
            "user_handle": user_handle,
        }

        response = silasdk.User.getVirtualAccounts(
            app, payload, eth_private_key)
        self.assertTrue(response["success"])

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

if __name__ == "__main__":
    unittest.main()
