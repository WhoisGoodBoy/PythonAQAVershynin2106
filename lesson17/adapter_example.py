import csv
import json

class CsvConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename:str):
        with open(filename, 'r') as csv_file:
            lines = csv.DictReader(csv_file)
            for line in lines:
                self.__lines.append((line))
        print(self.__lines)

    def write_to_file(self,filename:str):
        with open(filename, 'w') as writer:
            json.dump(self.__lines, writer, indent=4)
            self.cleanup()

    def cleanup(self):
        self.__lines = []


converter = CsvConverter()
converter.read_file("users.csv")
converter.write_to_file('users.json')

