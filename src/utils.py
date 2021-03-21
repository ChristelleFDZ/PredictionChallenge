import csv
from datetime import datetime



class DataParsing:

    def __init__(self,file_path, filename):
        self.file_path = file_path
        self.filename = filename

    def parseCSV(self):
        with open(self.file_path+"/"+self.filename, newline='') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')
            result_table = []
            for row in datareader:
                try:
                    result_table.append(RowData(row[0],row[1],row[2],row[3]))
                except ValueError as error:
                    print("Could not read row :( error: {0}".format(error))

            return result_table 


class RowData:

    def __init__(self, date, hour, total, daily):
        self.datetime = datetime.strptime(date + " " + hour, '%d/%m/%Y %H:%M:%S')
        self.total = int(total)
        self.daily = int(daily)
    
    def __str__(self):
        return self.datetime.strftime('%d/%m/%y %H:%M:%S') + " | " +str(self.total)+ " | " +str(self.daily)


        