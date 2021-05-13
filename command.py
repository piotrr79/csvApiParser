import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from env import EnvReader
from model.combine import CombineData
        
class Command:
    """ Command line command execution  """
    
    def __init__(self):
        self.debug = EnvReader.getDebugMode(self)
        self.csvPath = EnvReader.getCsvFolder(self)
        sys.tracebacklimit = self.debug
        
        
    def getArgs(self):
        """ Get arguments passed to command
            Returns:
                List of arguments
        """
        arguments = len(sys.argv) - 1
        
        # Command parameters validation
        if arguments < 2:
            raise Exception('Missing arguments. Please provide input and output csv file')
        
        if arguments > 2:
            raise Exception('Too many arguments. Please provide input and output csv file')

        response = []
        for i, arg in enumerate(sys.argv):
            if i != 0:
                response.append(arg)
 
        # Output file name validation
        if response[1].split('.')[-1]  != 'csv':
            raise Exception('Provided output file name is not valid csv file')
               
        return response


    def runCommand(self):
        """ Run command """
        params = self.getArgs()
        x = CombineData()
        # Return response from CombineData.combine() to be printed in cli
        return x.combine(self.csvPath + params[0], self.csvPath + params[1])
    
     
""" Command line call """       
x = Command()
output = x.runCommand()
#print(output)