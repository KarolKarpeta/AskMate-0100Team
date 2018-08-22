import persistence, util
import data_manager

# ------------------- QUESTION LIST -------------------------------------
def get_all_questions(): # get list of dictionaries, list of all questions
    try:
        return data_manager.get_all_questions()
    except FileNotFoundError as e:
        # logging.debug(e)
        return []

def get_all_answers(): # get list of dictionaries, list of all questions
    try:
        return data_manager.get_all_answers()
    except FileNotFoundError as e:
        # logging.debug(e)
        return []

# ------------------- DISPLAY QUESTION-------------------------------------


def get_question_by_id_logic(id): # get list of dictionaries, exacly 1 dictionary, 1 questions
    try:
        return data_manager.get_questions_by_id_dbm(id)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []


def get_answers_by_id_logic(id): # get list of dictionaries, all answers by q_id
    try:
        return data_manager.get_answers_by_question_id_dbm(id)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []



# ------------------- INSERT ANSWER -------------------------------------
def check_answer_length_logic(message):
    if util.correct_length(message, ">=", 10):
        # data_manager.add_new_question(inputs['title'],inputs['message'])
        return "Correct"
    else:
        return "Your message is too short. (Must be at least 10 characters long)"


def add_new_answer_logic(q_id, message): # insert new answer with exact question _id
    try:
        return data_manager.add_new_answer_db(q_id, message)   #get_answers_by_question_id_dbm(q_id, message)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []

# ------------------- DELETE ANSWER || DELETE QUESTION-------------------------------------
def delete_answer_logic(a_id): # delete answer with exact answer _id
    try:
        return data_manager.delete_answer_db(a_id)   #delete_answers_by_answers_id_dbm(a_id)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []

def delete_question_logic(q_id): # delete questionwith exact question _id
    try:
        return data_manager.delete_question_db(q_id)   #delete_question_by_question_id_dbm(q_id)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []

def delete_answer_logic_by_q_id(q_id):
    try:
        return data_manager.delete_answer_db_by_q_id(q_id)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []


# ------------------- INSERT QUESTION -------------------------------------

def check_length_message_question_db(inputs):
    if util.correct_length(inputs['message'], ">=", 10):
        data_manager.add_new_question(inputs['title'],inputs['message'])
        return "Correct"
    else:
        return "Your message is too short. (Must be at least 10 characters long)"



# ------------------- SEARCH QUESTION -------------------------------------

def search_question_logic(message):
    try:
        return data_manager.search_question_db(message)   #get_answers_by_question_id_dbm(q_id, message)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []


# ------------------- QUESTION VIEWS -------------------------------------
def get_question_view_logic(q_id):
    try:
        return data_manager.get_question_views_db(q_id)   #get_answers_by_question_id_dbm(q_id, message)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []

def set_question_view_logic(q_id, views_number):
    try:
        return data_manager.set_question_views_db(q_id, views_number)   #get_answers_by_question_id_dbm(q_id, message)
    except FileNotFoundError as e:
        # logging.debug(e)
        return []
