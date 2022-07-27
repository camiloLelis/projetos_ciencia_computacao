# from abc import ABC, abstractmethod


# class Inventory(ABC):
#     def __init__(self, path_file, type_report):
#         self.path_file = path_file
#         self.type_report = type_report

#     @abstractmethod
#     def import_data(self):
#         raise NotImplementedError


# class InventoryReportCSV(Inventory):
#     def import_data(self, path_file):
#         with open(self.path_file, 'r') as file:

import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory():
    @classmethod
    def import_data(cls, path_file, type_report):
        if path_file.endswith("csv"):
            data = []
            with open(path_file, 'r') as file:
                build_dict = csv.DictReader(file, delimiter=",", quotechar='"')
                for row in build_dict:
                    data.append(row)

        if path_file.endswith("json"):
            with open(path_file, 'r') as file:
                data = json.load(file)
                # print(data)

        cls.check_type_report(data, type_report)

    @classmethod
    def check_type_report(cls, data, type_report):
        if type_report == "simples":
            return SimpleReport.generate(data)
        if type_report == "completo":
            return CompleteReport.generate(data)


if __name__ == "__main__":
    csv_file = 'inventory_report/data/inventory.csv'
    print(Inventory.import_data(csv_file, "simples"))
    print(Inventory.import_data(csv_file, "completo"))
    json_file = 'inventory_report/data/inventory.json'
    print(Inventory.import_data(json_file, "simples"))
    print(Inventory.import_data(json_file, "completo"))
