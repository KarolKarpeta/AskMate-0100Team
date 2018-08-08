from datetime import datetime
import base64
import persistence
import uuid
import time


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

def generate_time_in_UNIX():
    my_list=[]
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    my_list.append(today)
    unix = time.mktime(datetime.strptime(today, "%Y-%m-%d %H:%M").timetuple())

    return int(unix)

def convert_unix_to_time_str(unix):
    norm_time= time.strftime("%Y-%m-%d %H:%M", time.localtime(int(unix)))

    return norm_time


def prepare_list_to_save_to_the_file(title, massage):
    generate_id()
    generate_time_in_UNIX()
    title_b64 = base64.b64encode(title.encode('utf-8'))
    massage_b64 = base64.b64encode(massage.encode('utf-8'))
    


    to_add=[id, str(unix), "0", "0",title_b64, massage_b64]
    return to_add

