import hashlib
import os
import unittest
import silasdk

from silasdk.tests.test_config import *


class Test005ZDocuments(unittest.TestCase):
    def test_list_supported_documents_200(self):

        response = silasdk.Documents.listSupportedDocuments(
            app, 1, 1)
        self.assertTrue(response["success"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["document_types"])

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
            "identity_type": "license"
        }

        response = silasdk.Documents.uploadDocument(
            app, payload, fileContents, eth_private_key)
        self.assertTrue(response["success"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["reference_id"])
        self.assertIsNotNone(response["document_id"])

        payload = {
            "user_handle": user_handle,
            "document_id": response["document_id"]
        }

        response = silasdk.Documents.getDocument(
            app, payload, eth_private_key)

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
        self.assertTrue(response["success"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertIsNotNone(response["documents"])
        self.assertIsNotNone(response["pagination"])


if __name__ == "__main__":
    unittest.main()
