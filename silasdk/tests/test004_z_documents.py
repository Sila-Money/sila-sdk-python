import unittest
import silasdk

from silasdk.tests.test_config import *


class Test004ZDocuments(unittest.TestCase):
    def test_upload_document_200(self):
        payload = {
            "file": "hello world",
            "user_handle": user_handle,
            "name": "CA drivers license",
            "file_name": "img_201901022_193206",
            "hash": "046a9aaa83711158c3c4afa585a30be3bee8a34231ee72caac625faef48b4abe",
            "mime_type": "image/jpeg",
            "document_type": "id_drivers_license",
            "identity_type": "license",
            "description": "my CA driver's license from 2019"
        }

        response = silasdk.Documents.uploadDocument(
            app, payload, eth_private_key)
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
        print(response)

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

    def test_list_supported_documents_200(self):

        response = silasdk.Documents.listSupportedDocuments(
            app, 1, 1)
        self.assertTrue(response["success"])
        self.assertEqual(response["status"], "SUCCESS")
        self.assertIsNotNone(response["message"])
        self.assertIsNotNone(response["document_types"])


if __name__ == "__main__":
    unittest.main()
