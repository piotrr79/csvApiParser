import os, csv
import unittest

class TestRunCommand(unittest.TestCase):
    """ Cli command tests 
        Command is triggered with os.system('command') which return 0 for success and non zero for failure
        Asserrts checks if result is equal / non equal 0, test for successful command execution checks also 
        generated csv file content against asserted content
    """
    
    @classmethod
    def setUpClass(self):
        """ Set test env variables """
        os.environ['DEBUG'] = '0'
        os.environ['CSV_PATH'] = 'tests/testsPayload/csvFiles/'
          
    def testCallCmdWrongOutput(self):
        """ Test for cmd with wrong output file
            Script throws error, assert cannot be 0 (success)
        """
        result = os.system('python3 command.py test_input.csv test_output')       
        self.assertNotEqual(0, result)
 
    def testCallCmdWrongInput(self):
        """ Test for cmd with wrong input file
            Script throws error, assert cannot be 0 (success)
        """
        result = os.system('command.py test_input test_output.csv')        
        self.assertNotEqual(0, result)   
 
    def testCallCmdMissingParams(self):
        """ Test for cmd with no paramters
            Script throws error, assert cannot be 0 (success)
        """
        result = os.system('python3 command.py')
        self.assertNotEqual(0, result)


    def testCallCmdMissingParam(self):
        """ Test for cmd with not enough paramters
            Script throws error, assert cannot be 0 (success)
        """
        result = os.system('python3 command.py test_input.csv')
        self.assertNotEqual(0, result)
    
    def testCallCmdTooManyParamsCsv(self):
        """ Test for cmd with too many paramters with csv extension
            Script throws error, assert cannot be 0 (success)
        """
        result = os.system('python3 command.py test_input.csv test_output.csv extra_param.csv')
        self.assertNotEqual(0, result)
        
    def testCallCmdTooManyParam(self):
        """ Test for cmd with too many paramters
            Script throws error, assert cannot be 0 (success)
        """
        result = os.system('python3 command.py test_input.csv test_output.csv extra_param')
        self.assertNotEqual(0, result)
        
    def testCallCmdWithEmptyInputFile(self):
        """ Test for cmd with empty input file
            Script throws error, assert cannot be 0 (success)
        """        
        result = os.system('python3 command.py test_empty_input.csv test_output.csv')               
        self.assertNotEqual(0, result)

    def testCallCmdWithApiError(self):
        """ Test for cmd successful csv call and Api error
            Script throws error (Api Exception), assert cannot be 0 (success)
        """        
        # Set Api Url to 404 one
        os.environ['API_URL'] = 'http://127.0.0.1:5000/'
        result = os.system('python3 command.py test_input.csv test_output.csv')              
        self.assertNotEqual(0, result)
        
    def testCallCmdSuccess(self):
        """ Test for cmd successful call
            Script returns success, assert is 0 (success)
            Second assert compares output file with assert, assert is True
        """        
        result = os.system('python3 command.py test_input.csv test_output.csv')               
        self.assertEqual(0, result)

        # Get created output csv file and transform it to output list
        outputFile = os.environ['CSV_PATH'] + 'test_output.csv'
        with open(outputFile, 'r') as file:
            reader = csv.reader(file)
            outputList = []
            for row in reader:
                outputList.append(row)
              
        # Set assert list  
        assertList = [['Account ID', 'Account Name', 'First Name', 'Created On', 'Status', 'Status Set On'], 
                       ['12345', 'acmecorp', 'Acme', '2011-01-12', 'good', '2011-01-12'], 
                       ['8172', 'johndoe', 'Doe', '2014-11-19', 'closed', '2015-09-01'], 
                       ['1924', 'lemurjulien', 'Julien', '2012-02-29', 'fraud', '2012-03-01'], 
                       ['222222', 'penguinsofmadagaskar', "kovalsky", '2012-03-01', 'poor', '2014-01-02'], 
                       ['48213', 'skipper', 'Skipper', '2015-07-07', 'high risk', '2015-08-15'], 
                       ['918299', 'mrheinz', 'MrHeinz', '2014-04-29', 'good', '2014-06-01'], 
                       ['88888', 'drmartens', 'Martens', '2013-08-08', 'collections', '2015-08-08']]
        
        # Compare output list with assert list
        if sorted(assertList) == sorted(outputList):
            listCompare = True
        else:
            listCompare = False
   
        self.assertEqual(True, listCompare)
        
        
    @classmethod
    def tearDownClass(self):
        """ Clear env variable to not interfere with prod values """
        os.environ['API_URL'] = ''
        os.environ['DEBUG'] = ''
        os.environ['CSV_PATH'] = ''
        
if __name__ == '__main__':
    unittest.main()