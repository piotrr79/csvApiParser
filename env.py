import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from decouple import config

class EnvReader():
    """ Get runtime params from env """
    
    def __init__(self):
        self

    def getApiUrl(self):
        """ Get api url form env 

            Returns:
                Api url string
        """
        if os.environ.get('API_URL') is not None:   
            self.apiUrl = os.environ['API_URL']
        else:
            self.apiUrl = config('API_URL')
        
        return self.apiUrl
    
    def getDebugMode(self):
        """ Get debug mode form env

            Returns:
                Debug mode int
        """
        if os.environ.get('DEBUG') is not None:   
            self.debug = os.environ['DEBUG']
        else:
            self.debug = config('DEBUG')
            
        return int(self.debug)
    
    def getCsvFolder(self):
        """ Get debug mode form env

            Returns:
                Csv path string
        """
        if os.environ.get('DECSV_PATHBUG') is not None:   
            self.csvPath = os.environ['CSV_PATH']
        else:
            self.csvPath = config('CSV_PATH')
            
        return self.csvPath