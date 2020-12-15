from .endpoints import endPoints
from silasdk import message


class Documents():
    def uploadDocument(self, payload, file, user_private_key):
        """
        Args:
            payload: document data
            user_private_key
        Returns:
            dict: response body (entity information)
        """
        path = endPoints["documents"]
        msg_type = "documents_msg"
        response = message.postRequest(
            self, path, msg_type, payload, key=user_private_key, content_type="multipart/form-data", file_contents=file)
        return response

    def listDocuments(self, payload, user_private_key, page=None, per_page=None, order=None):
        """
        Args:
            payload: document data
            user_private_key
        Returns:
            dict: response body (entity information)
        """
        path = endPoints["list_documents"] + \
            ('&page=' + str(page) if page is not None else '') + \
            ('&per_page=' + str(per_page) if per_page is not None else '') + \
            ('&order=' + order if order is not None else '')
        msg_type = "list_documents_msg"
        response = message.postRequest(
            self, path, msg_type, payload, user_private_key)
        return response

    def getDocument(self, payload, user_private_key):
        """
        Args:
            payload: document data
            user_private_key
        Returns:
            dict: response body (entity information)
        """
        path = endPoints["get_document"]
        msg_type = "get_document_msg"
        response = message.postGetFile(
            self, path, msg_type, payload, user_private_key)
        if (isinstance(response, dict)):
            return response
        else:
            document_reponse = {
                'status_code': response.status_code,
                'headers': response.headers,
                'content': response.content
            }
            return document_reponse

    def listSupportedDocuments(self, page=None, per_page=None):
        """
        Args:
            payload: document data
            user_private_key
        Returns:
            dict: response body (entity information)
        """
        payload = {}
        path = endPoints["list_supported_documents"] + \
            ('&page=' + str(page) if page is not None else '') + \
            ('&per_page=' + str(per_page) if per_page is not None else '')
        msg_type = "document_types_msg"
        response = message.postRequest(
            self, path, msg_type, payload)
        return response
