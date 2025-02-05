import csv

def open_file(path):
    """
    Open a CSV file from a given path and return it as a list
    """
    with open(path) as file:
        data_file = csv.reader(file, delimiter=",")
        next(data_file)
        data = list(data_file)
    return data
