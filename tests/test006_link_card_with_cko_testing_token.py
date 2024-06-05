import unittest
from silasdk.users import User
from tests.test_config import (app, user_handle_2, eth_private_key_2)


class Test006LinkCardWithCkoTestingToken(unittest.TestCase):
    def test_001_link_card_with_cko_testing_token_200(self):
        payload = {
                "card_number": 4659105569051157,
                "expiry_month": 12, 
                "expiry_year": 2027,
                "cvv": 956,
                "cko_public_key": "pk_sbox_i2uzy5w5nsllogfsc4xdscorcii"
            }   
        response = User.create_cko_testing_token(app, payload, eth_private_key_2)
        cko_token = response["token"]
        payload = {
            "user_handle": user_handle_2,
            "card_name": "visaas",
            "provider": "CKO",
            "token": cko_token
        }
        response = User.link_card(app, payload, eth_private_key_2)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response['status'],"SUCCESS")

    def test_001_link_card_with_cko_testing_token_400(self):
        payload = {
                "card_number": 4659105569051157,
                "expiry_month": 12, 
                "expiry_year": 2027,
                "cvv": 956,
                "cko_public_key": "pk_sbox_i2uzy5w5nsllogfsc4xdscorcii"
            }   
        response = User.create_cko_testing_token(app, payload, eth_private_key_2)
        payload = {
            "user_handle": user_handle_2,
            "card_name": "visaas",
            "provider": "CKO",
        }
        response = User.link_card(app, payload, eth_private_key_2)
        self.assertFalse(response["success"])
        self.assertEqual(response["status"], "FAILURE")
