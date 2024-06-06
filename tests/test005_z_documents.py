import hashlib
import os
import unittest
import silasdk

from tests.test_config import *


class Test005ZDocuments(unittest.TestCase):
    def test_list_supported_documents_200(self):

        response = silasdk.Documents.listSupportedDocuments(
            app, 1, 1)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["document_types"])
        self.assertIsNotNone(response["reference"])

    def test_upload_document_200(self):
        f = open(os.path.dirname(os.path.realpath(__file__)) +
                 "/images/logo-geko.png", "rb")
        fileContents = f.read()
        f.close()

        payload = {
            "user_handle": user_handle,
            "filename": "logo-geko",
            "hash": hashlib.sha256(fileContents).hexdigest(),
            "mime_type": "image/png",
            "document_type": "id_drivers_license",
            "identity_type": "license",
        }

        response = silasdk.Documents.uploadDocument(
            app, payload, fileContents, eth_private_key)
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["reference_id"])
        self.assertIsNotNone(response["document_id"])

        payload = {
            "user_handle": user_handle,
            "document_id": response["document_id"]
        }

        response = silasdk.Documents.getDocument(
            app, payload, eth_private_key)

        self.assertEquals(response['status_code'], 200)
        self.assertEquals(response['headers']['Content-Type'], 'image/png')
        self.assertIsNotNone(response['content'])

    def test_list_documents_200(self):
        payload = {
            "user_handle": user_handle,
            "start_date": "2020-01-01",
            "end_date": "2020-12-31",
            "doc_types": ["id_drivers_license"],
            "search": "my CA driver",
            "sort_by": "name",
        }

        response = silasdk.Documents.listDocuments(
            app, payload, eth_private_key, 1, 1, "asc")
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["documents"])
        self.assertIsNotNone(response["pagination"])
        self.assertIsNotNone(response["reference"])

    def test_upload_multiple_document_200(self):
        f = open(os.path.dirname(os.path.realpath(__file__)) +
                 "/images/logo-geko.png", "rb")
        fileContents_1 = f.read()
        f.close()

        a = open(os.path.dirname(os.path.realpath(__file__)) +
                 "/images/logo-geko.png", "rb")
        fileContents_2 = a.read()
        a.close()        

        
        payload = {
            "user_handle": user_handle,
            "file_metadata" : {
                "file_1":{                    
                    "filename": "logo-geko1",
                    "hash": hashlib.sha256(fileContents_1).hexdigest(),
                    "mime_type": "image/png",
                    "document_type": "id_drivers_license",
                    "identity_type": "license",
                },
                "file_2":{
                    "filename": "logo-geko1",
                    "hash": hashlib.sha256(fileContents_2).hexdigest(),
                    "mime_type": "image/png",
                    "document_type": "id_drivers_license",
                    "identity_type": "license",
                }
            }
        }
        
        fileContent = {
            "file_1" : fileContents_1,
            "file_2" : fileContents_2
        }
        
        response = silasdk.Documents.uploadDocuments(
            app, payload, fileContent, eth_private_key)         
        self.assertTrue(response.get('success'), msg=response.get('message', 'No message provided'))
        self.assertEqual(response["status"], "SUCCESS", msg=response.get('message', 'No message provided'))
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["reference_id"])
        self.assertIsNotNone(response["document_id"])

        payload = {
            "user_handle": user_handle
        }

        response = silasdk.Documents.listDocuments(
            app, payload, eth_private_key)        
        self.assertEquals(response['status_code'], 200)
        self.assertEquals(response['headers']['Content-Type'], 'application/json')

if __name__ == "__main__":
    unittest.main()
