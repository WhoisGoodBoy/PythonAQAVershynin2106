from .reader import Reader
from .csv_reader import CsvReader


class CsvProxyReader(Reader):
    def __init__(self, csv_reader:CsvReader):
        self.__result = ''
        self.__is_actual = False
        self.__reader = csv_reader


    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read()
            self.update_actual_status(True)
            return self.__result



    def update_actual_status(self, actual_status:bool):
        self.__is_actual = actual_status
