import unittest
from silasdk.users import User
from tests.test_config import (app, eth_private_key, plaid_token_for_card_url, plaid_token_for_card_payload, plaid_token_for_card_headers)


class Test006CreateCkoTestingToken(unittest.TestCase):

    def test_create_cko_testing_token_200(self):
        payload = {
                "card_number": 4095254802642505,
                "expiry_month": 12, 
                "expiry_year": 2027,
                "cvv": 956,
                "cko_public_key": "pk_sbox_i2uzy5w5nsllogfsc4xdscorcii"
            }   
        response = User.create_cko_testing_token(app, payload, eth_private_key)
        self.assertIsNotNone(response["token"])
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))

    def test_create_cko_testing_token_400(self):
        payload = {
                "card_number": 4095254802642505,
                "expiry_month": 12, 
                "expiry_year": 2027,
                "cvv": 956,
            }   
        response = User.create_cko_testing_token(app, payload, eth_private_key)
        self.assertFalse(response["success"])
        self.assertEqual(response["status"], "FAILURE")
