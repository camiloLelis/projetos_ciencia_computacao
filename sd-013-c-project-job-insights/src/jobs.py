from functools import lru_cache
import csv


@lru_cache
def read(path):
    list_jobs = []
    with open(path) as file:
        file_csv_dict = csv.DictReader(file, delimiter=",", quotechar='"')
        for linha in file_csv_dict:
            list_jobs.append(linha)
    return list_jobs


print(read("tests/mocks/jobs.csv"))
