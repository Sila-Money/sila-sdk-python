import unittest
import silasdk

from tests.test_config import *
from silasdk.users import User
from tests.test005_virtual_account import v_id, v_no
from silasdk.registrationFields import RegistrationFields


class Test100Teardown(unittest.TestCase):

    def test_aUnlink_business_member(self):
        payload = {
            "user_handle": user_handle,
            "business_handle": business_handle,
            "role": "administrator",
        }
        silasdk.BusinessOperations.unlinkBusinessMember(
            app, payload, eth_private_key, eth_private_key_3)

        payload = {
            "user_handle": user_handle,
            "business_handle": business_handle,
            "role": "controlling_officer",
        }
        silasdk.BusinessOperations.unlinkBusinessMember(
            app, payload, eth_private_key_2, eth_private_key_3)

        payload = {
            "user_handle": user_handle_2,
            "business_handle": business_handle,
            "role": "beneficial_owner",
        }
        silasdk.BusinessOperations.unlinkBusinessMember(
            app, payload, eth_private_key_2, eth_private_key_3)

    def test_close_virtual_account(self):

        payload = {
            "user_handle": user_handle,
            "virtual_account_id": v_id,
            "account_number": v_no
        }

        silasdk.User.closeVirtualAccount(
            app, payload, eth_private_key)

    def test_close_accounts_200(self):
        payload = {
            "user_handle": user_handle,
            "account_name": "default"
        }

        User.delete_account(
            app, payload, eth_private_key)

        payload = {
            "user_handle": user_handle,
            "account_name": "forupdate"
        }

        User.delete_account(
            app, payload, eth_private_key)\

        payload = {
            "user_handle": instant_ach_handle,
            "account_name": "default_plaid"
        }

        User.delete_account(
            app, payload, eth_private_key_4)

        payload = {
            "user_handle": sardine_handle,
            "account_name": "default_plaid"
        }

        User.delete_account(
            app, payload, eth_private_key_6)

        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid"
        }

        User.delete_account(
            app, payload, eth_private_key)

        payload = {
            "user_handle": user_handle,
            "account_name": "default_plaid2"
        }

        User.delete_account(
            app, payload, eth_private_key)

        payload = {
            "user_handle": user_handle,
            "account_name": "default_mx"
        }

        User.delete_account(
            app, payload, eth_private_key)

    def test_delete_restration_data(self):

        payload = {
            "user_handle": user_handle
        }

        response = User.get_entity(app, payload, eth_private_key)
        email_uuid = response["emails"][0]["uuid"]
        phone_uuid = response["phones"][0]["uuid"]
        address_uuid = response["addresses"][0]["uuid"]

        payload = {
            "user_handle": user_handle,
            "uuid": address_uuid
        }

        User.deleteRegistrationData(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)
        
        payload = {
            "user_handle": user_handle,
            "uuid": phone_uuid
        }

        User.deleteRegistrationData(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)
        payload = {
            "user_handle": user_handle,
            "uuid": email_uuid
        }

        User.deleteRegistrationData(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)

        payload = {
            "user_handle": business_handle
        }

        response = User.get_entity(app, payload, eth_private_key_3)
        email_uuid = response["emails"][0]["uuid"]
        phone_uuid = response["phones"][0]["uuid"]
        address_uuid = response["addresses"][0]["uuid"]

        payload = {
            "user_handle": business_handle,
            "uuid": address_uuid
        }

        User.deleteRegistrationData(
            app, RegistrationFields.ADDRESS, payload, eth_private_key_3)

        payload = {
            "user_handle": business_handle,
            "uuid": phone_uuid
        }

        User.deleteRegistrationData(
            app, RegistrationFields.ADDRESS, payload, eth_private_key_3)

        payload = {
            "user_handle": business_handle,
            "uuid": email_uuid
        }

        User.deleteRegistrationData(
            app, RegistrationFields.ADDRESS, payload, eth_private_key_3)
