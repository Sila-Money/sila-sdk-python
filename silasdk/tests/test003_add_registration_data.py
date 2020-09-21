import unittest
import silasdk

from silasdk.tests.test_config import *


class Test003AddRegistrationDataTest(unittest.TestCase):
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

        response = silasdk.User.deleteRegistrationData(app, silasdk.RegistrationFields.IDENTITY, payload, eth_private_key_3)

        identityAlias = "EIN"
        identityValue = "543212222"
        payload = {
            "user_handle": business_handle,
            "identity_alias": identityAlias,
            "identity_value": identityValue
        }

        response = silasdk.User.addRegistrationData(app, silasdk.RegistrationFields.IDENTITY, payload, eth_private_key_3)
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

if __name__ == "__main__":
    unittest.main()
