import base64
import persistence
import uuid


def string_to_base64(s):
    return base64.b64encode(s.encode('utf-8'))


def base64_to_string(b):
    return base64.b64decode(b).decode('utf-8')


def get_headers_on_main_site(a):
    headers = persistence.import_headers("sample_data/question.csv")
    new_dic__ist = []
    for row in a:
        new_dic__ist.append(dict((key, value) for key, value in row.items() if key in headers[:5]))
    return new_dic__ist


def generate_id():
    id = uuid.uuid4()
    return id
