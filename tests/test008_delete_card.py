import unittest
import uuid
from unittest import mock

from silasdk.users import User
from tests.test_config import (app, user_handle, eth_private_key, eth_private_key_2)


class Test008DeleteCardTest(unittest.TestCase):
    @mock.patch('silasdk.message.postRequest',
                return_value={'success': True, 'reference': str(uuid.uuid4())})
    def test_002_delete_card_200(self, _):
        payload = {
            "user_handle": user_handle,
            "card_name": "delete",
            "provider": "CKO"
        }

        response = User.delete_card(app, payload, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["reference"])

    def test_003_delete_card_400(self):
        payload = {
            "user_handle": '',
            "card_name": "visaas",           
        }

        response = User.delete_card(app, payload, eth_private_key_2)
        self.assertFalse(response["success"])  



if __name__ == "__main__":
    unittest.main()
