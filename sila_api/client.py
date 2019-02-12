from .http_client import HttpClient



class Client(HttpClient):

    def __init__(self,url,developer_key,user_key):
        
        self.url=url
        self.developer_key=developer_key
        self.user_key=user_key
        self.httpClient=HttpClient()



    


   


   
