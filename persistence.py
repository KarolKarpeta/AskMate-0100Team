import csv


def import_from_file(file_name):
    dictList = []
    with open(file_name, 'r') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            dictList.append(row)
        return dictList


print(import_from_file('sample_data/question.csv'))

def import_headers(file_name):
    with open(file_name, 'r') as csv_file:
        reader=csv.reader(csv_file)
        for header_line in reader:
            return header_line
