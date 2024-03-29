from datetime import datetime
import base64
import persistence
import uuid
import time


def string_to_base64(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')


def base64_to_string(b):
    return base64.b64decode(b.encode('utf-8')).decode('utf-8')


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
    id = generate_id()
    unix = generate_time_in_UNIX()
    title_b64 = base64.b64encode(title.encode('utf-8'))
    massage_b64 = base64.b64encode(massage.encode('utf-8'))


def correct_length(text, validator, length):
    """
    Checking if text has valid length.

    Args:
    text(string): String that will be checked for its length
    validator(string): Operator used to check text vs length(saved in a string)
    length(integer): Value checked vs length of text

    Returns: 
    True or False
    """

    return eval("len(text) {} length".format(validator))


def prepare_list_to_save_to_the_file(title, massage):
    id_ = generate_id()
    unix = generate_time_in_UNIX()
    #title_b64 = base64.b64encode(title.encode('utf-8'))
    #massage_b64 = base64.b64encode(massage.encode('utf-8'))
    
    to_add=[id_, str(unix), "0", "0", title, massage,]
    return to_add

def split_list_of_dictionaries(list_of_dictionaries):

    list_of_list = []
    questions = []
    answers = []
    comments = []

    for dic in list_of_dictionaries:
        for key, value in dic.items():
            if value == 'answer':
                answers.append(dic)
            elif value == 'question':
                questions.append(dic)
            elif value == 'comment':
                comments.append(dic)

    print("lista", list_of_dictionaries)

    list_of_list.append(questions)
    list_of_list.append(answers)
    list_of_list.append(comments)


    return list_of_list

