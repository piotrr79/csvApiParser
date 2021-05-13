import csv, os

class CsvData:
    """ Csv files parser """
    
    def __init__(self):
        self

    def readCsv(self, resource):
        """ Read csv content and return list with rows
        
            Args:
            self: Self.
            resource: Csv file resource.

            Returns:
                List of lists
        """
        with open(resource, 'r') as file:
            try:
                reader = csv.reader(file)
            except Exception as err:          
                return str(err)
        
            if os.stat(resource).st_size == 0:
                raise Exception('Provided input file is empty')
        
            response = []
            for row in reader:
                response.append(row)
            
            return response

    def writeCsv(self, data, resource):
        """ Write csv file with content from data  
               
            Args:
            self: Self.
            data: List of lists with data to write to csv
            resource: Csv file name for output.

            Returns:
                Csv file
        """
        with open(resource, 'w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for item in data:
                writer.writerow(item)
            
            return writer