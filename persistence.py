import csv

q_headers = ["id","submission_time","view_number","vote_number","title","message","image"]

def import_from_file(file_name):
    dictList = []
    with open(file_name, 'r') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            dictList.append(row)
    for lists in dictList:
        for key , value in lists.items():
            if key == 'submission_time':
                value_normal=time.strftime("%Y-%m-%d %H:%M", time.localtime(int(value)))
                lists[key]=value_normal
    return dictList


print(import_from_file('sample_data/question.csv'))


def import_headers(file_name):
    with open(file_name, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for header_line in reader:
            return header_line


def export_data_to_file(path, data):
    with open(path, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        # for line in data:
        writer.writerow(data)
        print("persistence_add_question")


def write_data_to_file(file_name, fieldnames, data):
    with open(file_name, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames)
        csv_writer.writerow(data)



