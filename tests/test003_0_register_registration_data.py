import unittest
import uuid

from silasdk.registrationFields import RegistrationFields
from silasdk.users import User
from tests.test_config import (
    app, business_handle, eth_private_key, user_handle, eth_private_key_3, sardine_handle, eth_private_key_6, business_handle_2, eth_private_key_7)


class Test003RegistrationDataTests(unittest.TestCase):

    def test_add_registration_data_200(self):
        email = "fake2@email.com"
        payload = {
            "user_handle": user_handle,
            "email": email,
        }

        response = User.add_registration_data(
            app, RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["email"]["email"], email)
        self.assertIsNotNone(response["email"]["added_epoch"])
        self.assertIsNotNone(response["email"]["modified_epoch"])
        self.assertIsNotNone(response["email"]["uuid"])
        self.assertIsNotNone(response["reference"])

        phone = "3189250987"
        payload = {
            "user_handle": user_handle,
            "phone": phone,
            "sms_opt_in": True
        }

        response = User.add_registration_data(
            app, RegistrationFields.PHONE, payload, eth_private_key)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["phone"]["phone"], phone)
        self.assertIsNotNone(response["phone"]["added_epoch"])
        self.assertIsNotNone(response["phone"]["modified_epoch"])
        self.assertIsNotNone(response["phone"]["uuid"])
        self.assertTrue(response.get('phone').get(
            'sms_confirmation_requested'))
        self.assertIsNotNone(response["reference"])


        payload = {
            "user_handle": business_handle
        }

        response = User.get_entity(app, payload, eth_private_key_3)
        identity_uuid = response["identities"][0]["uuid"]
        payload = {
            "user_handle": business_handle,
            "uuid": identity_uuid
        }

        response = User.deleteRegistrationData(
            app, RegistrationFields.IDENTITY, payload, eth_private_key_3)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

        identity_alias = "EIN"
        identity_value = "543212222"
        payload = {
            "user_handle": business_handle,
            "identity_alias": identity_alias,
            "identity_value": identity_value
        }

        response = User.add_registration_data(
            app, RegistrationFields.IDENTITY, payload, eth_private_key_3)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["identity"]["identity_type"], identity_alias)
        self.assertIsNotNone(response["identity"]["identity"])
        self.assertIsNotNone(response["identity"]["added_epoch"])
        self.assertIsNotNone(response["identity"]["modified_epoch"])
        self.assertIsNotNone(response["identity"]["uuid"])
        self.assertIsNotNone(response["reference"])

        address_alias = "added address"
        street_address_1 = "324 songbird avenue"
        street_address_2 = "apt. 132"
        state = "va"
        postal_code = "12345"
        country = "US"
        city = "portland"
        payload = {
            "user_handle": user_handle,
            "address_alias": address_alias,
            "street_address_1": street_address_1,
            "street_address_2": street_address_2,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "country": country
        }

        response = User.add_registration_data(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["address"]["nickname"], address_alias)
        self.assertEqual(response["address"]
                         ["street_address_1"], street_address_1)
        self.assertEqual(response["address"]
                         ["street_address_2"], street_address_2)
        self.assertEqual(response["address"]["city"], city)
        self.assertEqual(response["address"]["state"], state)
        self.assertEqual(response["address"]["postal_code"], postal_code)
        self.assertEqual(response["address"]["country"], country)
        self.assertIsNotNone(response["address"]["added_epoch"])
        self.assertIsNotNone(response["address"]["modified_epoch"])
        self.assertIsNotNone(response["address"]["uuid"])
        self.assertIsNotNone(response["reference"])

        payload = {
            'user_handle': user_handle,
            'device_fingerprint': 'test_device_fingerprint_added'
        }

        response = User.add_registration_data(
            app, RegistrationFields.DEVICE, payload, eth_private_key)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertRegex(response.get('message'),
                         r'\bsuccessfully registered for handle\b')
        self.assertEqual(response.get('status_code'), 200)
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

    def test_add_registration_data_400(self):
        payload = {
            "user_handle": user_handle,
        }

        response = User.add_registration_data(
            app, RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.add_registration_data(
            app, RegistrationFields.PHONE, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.add_registration_data(
            app, RegistrationFields.IDENTITY, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.add_registration_data(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_update_registration_data_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = User.get_entity(app, payload, eth_private_key)

        email_uuid = response["emails"][0]["uuid"]
        phone_uuid = response["phones"][0]["uuid"]
        identity_uuid = response["identities"][0]["uuid"]
        address_uuid = response["addresses"][0]["uuid"]

        email = "fake3@email.com"
        payload = {
            "user_handle": user_handle,
            "email": email,
            "uuid": email_uuid
        }

        response = User.update_registration_data(
            app, RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["email"]["email"], email)
        self.assertEqual(response["email"]["uuid"], email_uuid)
        self.assertIsNotNone(response["email"]["added_epoch"])
        self.assertIsNotNone(response["email"]["modified_epoch"])
        self.assertIsNotNone(response["reference"])

        phone = "3189250988"
        payload = {
            "user_handle": user_handle,
            "phone": phone,
            "uuid": phone_uuid,
            'sms_opt_in': False
        }

        response = User.update_registration_data(
            app, RegistrationFields.PHONE, payload, eth_private_key)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["phone"]["phone"], phone)
        self.assertIsNotNone(response["phone"]["added_epoch"])
        self.assertIsNotNone(response["phone"]["modified_epoch"])
        self.assertIsNotNone(response["reference"])

        identity_alias = "SSN"
        identity_value = "543212223"
        payload = {
            "user_handle": user_handle,
            "identity_alias": identity_alias,
            "identity_value": identity_value,
            "uuid": identity_uuid
        }

        response = User.update_registration_data(
            app, RegistrationFields.IDENTITY, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["identity"]["identity_type"], identity_alias)
        self.assertIsNotNone(response["identity"]["identity"])
        self.assertIsNotNone(response["identity"]["added_epoch"])
        self.assertIsNotNone(response["identity"]["modified_epoch"])
        self.assertIsNotNone(response["identity"]["uuid"])
        self.assertIsNotNone(response["reference"])

        address_alias = "added address"
        street_address_1 = "324 Songbird Avenue"
        street_address_2 = "Apt. 132"
        state = "VA"
        postal_code = "12345"
        country = "US"
        city = "Portland"
        payload = {
            "user_handle": user_handle,
            "address_alias": address_alias,
            "street_address_1": street_address_1,
            "street_address_2": street_address_2,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "country": country,
            "uuid": address_uuid
        }

        response = User.update_registration_data(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["address"]["nickname"], address_alias)
        self.assertEqual(response["address"]
                         ["street_address_1"], street_address_1)
        self.assertEqual(response["address"]
                         ["street_address_2"], street_address_2)
        self.assertEqual(response["address"]["city"], city)
        self.assertEqual(response["address"]["state"], state)
        self.assertEqual(response["address"]["postal_code"], postal_code)
        self.assertEqual(response["address"]["country"], country)
        self.assertIsNotNone(response["address"]["added_epoch"])
        self.assertIsNotNone(response["address"]["modified_epoch"])
        self.assertIsNotNone(response["reference"])

        first_name = "NewFirst"
        last_name = "NewLast"
        entity_name = "NewFirst NewLast"
        birthdate = "1994-01-01"

        payload = {
            "user_handle": user_handle,
            "first_name": first_name,
            "last_name": last_name,
            "entity_name": entity_name,
            "birthdate": birthdate
        }

        response = User.update_registration_data(
            app, RegistrationFields.ENTITY, payload, eth_private_key)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["user_handle"], user_handle)
        self.assertEqual(response["entity_type"], "individual")
        self.assertEqual(response["entity"]["entity_name"], entity_name)
        self.assertEqual(response["entity"]["birthdate"], birthdate)
        self.assertEqual(response["entity"]["first_name"], first_name)
        self.assertEqual(response["entity"]["last_name"], last_name)
        self.assertIsNotNone(response["entity"]["created_epoch"])
        self.assertIsNotNone(response["reference"])

        entity_name = "NewCompany"
        birthdate = "1994-01-01"
        business_type = "corporation"
        naics_code = 721
        doing_business_as = "NC Limited"
        business_website = "https://newwebsite.domain"
        registration_state = "NY"

        payload = {
            "user_handle":  business_handle,                        
            "entity_name": entity_name,
            "birthdate": birthdate,
            "business_type": business_type,
            "naics_code": naics_code,
            "doing_business_as": doing_business_as,
            "business_website": business_website,
            "registration_state": registration_state
        }

        response = User.update_registration_data(
            app, RegistrationFields.ENTITY, payload, eth_private_key_3)        
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertEqual(response["user_handle"], business_handle)
        self.assertEqual(response["entity_type"], "business")
        self.assertEqual(response["entity"]["entity_name"], entity_name)
        self.assertEqual(response["entity"]["birthdate"], birthdate)
        self.assertEqual(response["entity"]["business_type"], business_type)
        self.assertEqual(response["entity"]["naics_code"], naics_code)
        self.assertEqual(response["entity"]
                         ["doing_business_as"], doing_business_as)
        self.assertEqual(response["entity"]
                         ["business_website"], business_website)
        self.assertIsNotNone(response["entity"]["created_epoch"])
        self.assertIsNotNone(response["entity"]["business_uuid"])
        self.assertIsNotNone(response["entity"]["naics_category"])
        self.assertIsNotNone(response["entity"]["naics_subcategory"])
        self.assertIsNotNone(response["reference"])

    def test_update_registration_data_400(self):
        payload = {
            "user_handle": user_handle,
        }

        response = User.update_registration_data(
            app, RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.update_registration_data(
            app, RegistrationFields.PHONE, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.update_registration_data(
            app, RegistrationFields.IDENTITY, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.update_registration_data(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_delete_registration_data_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = User.get_entity(app, payload, eth_private_key)

        email_uuid = response["emails"][0]["uuid"]
        phone_uuid = response["phones"][0]["uuid"]
        address_uuid = response["addresses"][0]["uuid"]

        payload = {
            "user_handle": user_handle,
            "uuid": email_uuid
        }

        response = User.deleteRegistrationData(
            app, RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

        payload = {
            "user_handle": user_handle,
            "uuid": phone_uuid
        }

        response = User.deleteRegistrationData(
            app, RegistrationFields.PHONE, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

        payload = {
            "user_handle": user_handle,
            "uuid": address_uuid
        }

        response = User.deleteRegistrationData(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

    def test_delete_registration_data_400(self):
        payload = {
            "user_handle": user_handle,
        }

        response = User.deleteRegistrationData(
            app, RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.deleteRegistrationData(
            app, RegistrationFields.PHONE, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.deleteRegistrationData(
            app, RegistrationFields.IDENTITY, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = User.deleteRegistrationData(
            app, RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")


    def test_add_registration_data_session_identifier_200(self):
        session_identifier = str(uuid.uuid4())
        payload = {
            "user_handle": user_handle,
            "session_identifier": session_identifier,
            "device_fingerprint": "test_sardine_integration"
        }

        response = User.add_registration_data(
            app, RegistrationFields.DEVICE, payload, eth_private_key)

        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

if __name__ == "__main__":
    unittest.main()
