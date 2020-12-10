import unittest
import silasdk

from tests.test_config import *


class Test003RegistrationDataTests(unittest.TestCase):

    def test_add_registration_data_200(self):
        email = "fake2@email.com"
        payload = {
            "user_handle": user_handle,
            "email": email,
        }

        response = silasdk.User.addRegistrationData(
            app, silasdk.RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["email"]["email"], email)
        self.assertIsNotNone(response["email"]["added_epoch"])
        self.assertIsNotNone(response["email"]["modified_epoch"])
        self.assertIsNotNone(response["email"]["uuid"])

        phone = "3189250987"
        payload = {
            "user_handle": user_handle,
            "phone": phone,
        }

        response = silasdk.User.addRegistrationData(
            app, silasdk.RegistrationFields.PHONE, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["phone"]["phone"], phone)
        self.assertIsNotNone(response["phone"]["added_epoch"])
        self.assertIsNotNone(response["phone"]["modified_epoch"])
        self.assertIsNotNone(response["phone"]["uuid"])

        payload = {
            "user_handle": business_handle
        }

        response = silasdk.User.getEntity(app, payload, eth_private_key_3)
        identityUuid = response["identities"][0]["uuid"]
        payload = {
            "user_handle": business_handle,
            "uuid": identityUuid
        }

        response = silasdk.User.deleteRegistrationData(
            app, silasdk.RegistrationFields.IDENTITY, payload, eth_private_key_3)

        identityAlias = "EIN"
        identityValue = "543212222"
        payload = {
            "user_handle": business_handle,
            "identity_alias": identityAlias,
            "identity_value": identityValue
        }

        response = silasdk.User.addRegistrationData(
            app, silasdk.RegistrationFields.IDENTITY, payload, eth_private_key_3)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["identity"]["identity_type"], identityAlias)
        self.assertIsNotNone(response["identity"]["identity"])
        self.assertIsNotNone(response["identity"]["added_epoch"])
        self.assertIsNotNone(response["identity"]["modified_epoch"])
        self.assertIsNotNone(response["identity"]["uuid"])

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
            "country": country
        }

        response = silasdk.User.addRegistrationData(
            app, silasdk.RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
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

    def test_add_registration_data_400(self):
        payload = {
            "user_handle": user_handle,
        }

        response = silasdk.User.addRegistrationData(
            app, silasdk.RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.addRegistrationData(
            app, silasdk.RegistrationFields.PHONE, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.addRegistrationData(
            app, silasdk.RegistrationFields.IDENTITY, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.addRegistrationData(
            app, silasdk.RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_update_registration_data_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = silasdk.User.getEntity(app, payload, eth_private_key)

        emailUuid = response["emails"][0]["uuid"]
        phoneUuid = response["phones"][0]["uuid"]
        identityUuid = response["identities"][0]["uuid"]
        addressUuid = response["addresses"][0]["uuid"]

        email = "fake3@email.com"
        payload = {
            "user_handle": user_handle,
            "email": email,
            "uuid": emailUuid
        }

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["email"]["email"], email)
        self.assertEqual(response["email"]["uuid"], emailUuid)
        self.assertIsNotNone(response["email"]["added_epoch"])
        self.assertIsNotNone(response["email"]["modified_epoch"])

        phone = "3189250988"
        payload = {
            "user_handle": user_handle,
            "phone": phone,
            "uuid": phoneUuid
        }

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.PHONE, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["phone"]["phone"], phone)
        self.assertIsNotNone(response["phone"]["added_epoch"])
        self.assertIsNotNone(response["phone"]["modified_epoch"])

        identityAlias = "SSN"
        identityValue = "543212223"
        payload = {
            "user_handle": user_handle,
            "identity_alias": identityAlias,
            "identity_value": identityValue,
            "uuid": identityUuid
        }

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.IDENTITY, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["identity"]["identity_type"], identityAlias)
        self.assertIsNotNone(response["identity"]["identity"])
        self.assertIsNotNone(response["identity"]["added_epoch"])
        self.assertIsNotNone(response["identity"]["modified_epoch"])
        self.assertIsNotNone(response["identity"]["uuid"])

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
            "uuid": addressUuid
        }

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
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

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.ENTITY, payload, eth_private_key)

        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertEqual(response["user_handle"], user_handle)
        self.assertEqual(response["entity_type"], "individual")
        self.assertEqual(response["entity"]["entity_name"], entity_name)
        self.assertEqual(response["entity"]["birthdate"], birthdate)
        self.assertEqual(response["entity"]["first_name"], first_name)
        self.assertEqual(response["entity"]["last_name"], last_name)
        self.assertIsNotNone(response["entity"]["created_epoch"])

        entity_name = "NewCompany"
        birthdate = "1994-01-01"
        business_type = "corporation"
        naics_code = 721
        doing_business_as = "NC Limited"
        business_website = "https://newwebsite.domain"

        payload = {
            "user_handle": business_handle,
            "entity_name": entity_name,
            "birthdate": birthdate,
            "business_type": business_type,
            "naics_code": naics_code,
            "doing_business_as": doing_business_as,
            "business_website": business_website
        }

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.ENTITY, payload, eth_private_key_3)

        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")
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

    def test_update_registration_data_400(self):
        payload = {
            "user_handle": user_handle,
        }

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.PHONE, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.IDENTITY, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.updateRegistrationData(
            app, silasdk.RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

    def test_delete_registration_data_200(self):
        payload = {
            "user_handle": user_handle
        }

        response = silasdk.User.getEntity(app, payload, eth_private_key)

        emailUuid = response["emails"][0]["uuid"]
        phoneUuid = response["phones"][0]["uuid"]
        identityUuid = response["identities"][0]["uuid"]
        addressUuid = response["addresses"][0]["uuid"]

        payload = {
            "user_handle": user_handle,
            "uuid": emailUuid
        }

        response = silasdk.User.deleteRegistrationData(
            app, silasdk.RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")

        payload = {
            "user_handle": user_handle,
            "uuid": phoneUuid
        }

        response = silasdk.User.deleteRegistrationData(
            app, silasdk.RegistrationFields.PHONE, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")

        payload = {
            "user_handle": user_handle,
            "uuid": addressUuid
        }

        response = silasdk.User.deleteRegistrationData(
            app, silasdk.RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertTrue(response["success"])
        self.assertIsNotNone(response["message"])
        self.assertEqual(response["status"], "SUCCESS")

    def test_delete_registration_data_400(self):
        payload = {
            "user_handle": user_handle,
        }

        response = silasdk.User.deleteRegistrationData(
            app, silasdk.RegistrationFields.EMAIL, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.deleteRegistrationData(
            app, silasdk.RegistrationFields.PHONE, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.deleteRegistrationData(
            app, silasdk.RegistrationFields.IDENTITY, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")

        response = silasdk.User.deleteRegistrationData(
            app, silasdk.RegistrationFields.ADDRESS, payload, eth_private_key)
        self.assertEqual(response["status"], "FAILURE")


if __name__ == "__main__":
    unittest.main()
