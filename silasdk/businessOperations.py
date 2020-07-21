from .endpoints import endPoints
from .client import App
from silasdk import message


class BusinessOperations():

    def linkBusinessMember(self, payload, user_private_key, business_private_key):
        """
        Args:
            payload: includes member information.
            user_private_key:
            business_private_key:
        Returns:
            dict: response body (confirmation message)
        """
        path = endPoints["linkBusinessMember"]
        msg_type = "link_business_member_msg"
        response = message.postRequest(self, path, msg_type, payload, user_private_key, business_private_key)
        return response
