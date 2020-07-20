from .endpoints import endPoints
from .client import App
from silasdk import message


class BusinessInformation():

    def getBusinessTypes(self):
        """Gets a list of valid business types that can be registered.
        Args:
        Returns:
            dict: response body (business types)
        """
        path = endPoints["getBusinessTypes"]
        msg_type = "business_types_msg"
        payload = {}
        response = message.postRequest(self, path, msg_type, payload)
        return response
