import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from decouple import config
from env import EnvReader
from apidata.parser import ApiData
from csvdata.parser import CsvData

class CombineData():
    """ Get CSV and Api data and combine them """
    
    def __init__(self):
        self.csvData = CsvData()
        self.apiData = ApiData()
        self.apiUrl = EnvReader.getApiUrl(self)

    def combine(self, input_file, output_file):
        """ Combine Api and Csv data
                       
            Args:
            self: Self.
            input_file: Input csv file
            output_file: Output csv file

            Returns:
                String response
        """
        
        csvOutput = self.csvData.readCsv(input_file)
        
        # Extract csv column names
        columnsNmes = csvOutput[0]
        
        response = []
        
        # Remove first row from csv output (columns names)
        iterCsvOutput = iter(csvOutput)
        next(iterCsvOutput)
        # Get all api data with one call
        apiResponse =  self.apiData.getContent(self.apiUrl)

        # Iterate over Csv lines
        for item in iterCsvOutput:      

            # For each CSV line find corresponding account in Api response
            for apiItem in apiResponse['results']:

                # I Api response match Csv row combine data
                if str(apiItem['account_id']) == item[0]:           
                    # Add response form Api
                    item.insert(4, apiItem['status'])
                    item.insert(5, apiItem['created_on'])
                    response.append(item)
        
        # Add row with new column names
        columnsNmes.insert(4, 'Status')
        columnsNmes.insert(5, 'Status Set On')
        response.insert(0, columnsNmes)

        # Generate csv output file
        self.csvData.writeCsv(response, output_file)
        
        return 'Given output file has been generated'