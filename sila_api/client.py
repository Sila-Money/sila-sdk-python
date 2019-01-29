import requests

from .http_client import HttpClient
import requests
import logging
from .user import User
from .transactions import Transactions

class Client():
    
    
    def  __init__(self,base_url):

        self.http=HttpClient(
            self.base_url=base_url
        )