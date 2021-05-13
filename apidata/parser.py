import requests
import json

class ApiData:
    """ Api parser """
    
    def __init__(self):
        self
        
    def getUrlData(self, url):
        """ Get data from api  

            Args:
            self: Self.
            url: Api url

            Returns:
                Http resource content
        """
        try:
            return requests.get(url)
        except Exception as err:          
            return str(err)
        
    def getContent(self, url):
        """ Parse data from api channel 
               
            Args:
            self: Self.
            url: Api url

            Returns:
                Json content
        """
        data = self.getUrlData(url)
        if data.status_code == 200: 
            return data.json()
        else:
            raise Exception('Api did not return valid response')
