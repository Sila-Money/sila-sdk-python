import unittest
import silasdk
import requests
import json

from tests.test_config import ( sardine_handle, eth_private_key_6,
    app, eth_private_key, eth_private_key_4, instant_ach_handle, user_handle)


class Test006LinkAccountTest(unittest.TestCase):
    def test_link_account_200(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "default",
            "account_number": "123456789012",
            "routing_number": "123456780",
            "account_type": "CHECKING",
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, False)
        
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response['web_debit_verified'])
        
        payload = {
            "user_handle": user_handle,
            "account_name": "unlink",
            "account_number": "123456789013",
            "routing_number": "123456780",
            "account_type": "CHECKING",
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, False)
        
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))

        payload = {
            "user_handle": user_handle,
            "account_name": "forupdate",
            "account_number": "123456789013",
            "routing_number": "123456780",
            "account_type": "CHECKING",
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, False)
        
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))

    def test_link_account_instant_ach(self):
        payload = {
            "user_handle": instant_ach_handle,
            "account_name": "default_plaid",
            "plaid_token": "sandbox"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key_4, True)
        
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))

    def test_link_account_sardine(self):
        payload = {
            "user_handle": sardine_handle,
            "account_name": "default_plaid",
            "plaid_token": "sandbox"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key_6, True)
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))

    def test_link_account_plaid_200(self):
        options = {
            "public_key": "fa9dd19eb40982275785b09760ab79",
            "initial_products": ["transactions"],
            "institution_id": "ins_109508",
            "credentials": {
                "username": "user_good",
                "password": "pass_good"
            }
        }

        plaid_response = app.postPlaid(
            "https://sandbox.plaid.com/link/item/create", options)
        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid",
            "public_token": plaid_response["public_token"],
            "selected_account_id": plaid_response["accounts"][0]["account_id"],
            "message": "link_account_msg"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, True)

        
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response['account_owner_name'])

        plaid_response = app.postPlaid(
            "https://sandbox.plaid.com/link/item/create", options)
        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid2",
            "plaid_token": plaid_response["public_token"],
            "message": "link_account_msg",
            "plaid_token_type": "legacy"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, True)

        
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response['account_owner_name'])

    def test_link_account_400(self):
        payload = {
            "account_name": "default",
            "plaid_token": ""
        }

        response = silasdk.User.linkAccount(app, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_link_account_mx_200(self):
        payload = {
            "user_handle": user_handle,
            "provider": "mx",
            "provider_token_type": 'processor',
            "provider_token": self.generate_provider_token(),
            "account_name": 'default_mx',
            "selected_account_id": "7689870149"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, False,True)
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))

    def test_link_account_mx_400(self):
        payload = {
            "provider": "mx",
            "provider_token_type": 'processor',
            "provider_token":'fgnbvchjdftyluikmn-5bk84',
            "selected_account_id": "7689870149"
        }

        response = silasdk.User.linkAccount(
            app, payload, eth_private_key, False,True)
        self.assertEqual(response["status"], "FAILURE")

    def generate_provider_token(self):
        url = "https://int-api.mx.com/payment_processor_authorization_code"

        payload = json.dumps({
            "payment_processor_authorization_code": {
                "user_guid": "USR-78912abf-a65b-4661-806b-bdcf4e062e16",
                "member_guid": "MBR-1e0d03f3-d42e-46e7-86fb-ae07b79c557a",
                "account_guid": "ACT-cc129199-606c-41a3-aeec-ee32980362d4"
            }
        })
        headers = {
            'Accept':'application/vnd.mx.api.v1+json',
            'Authorization': 'Basic OWNlOTFhZWQtMDA4Zi00YjFmLThlMzktNGU3YTU5NjZlOTVhOmYyZThkYzE4MmY2MzQ5OTk5NjMzMDJlYTE3OGU3NTBkZWU2NDQ3ODM=',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        provider_token = (response.json().get("payment_processor_authorization_code").get("authorization_code"))

        return provider_token


if __name__ == '__main__':
    unittest.main()
