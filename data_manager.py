import database_common
import util

@database_common.connection_handler # Get all questions from database
def get_all_questions(cursor):

    cursor.execute("""SELECT * FROM question; """)  # get question data
    all_questions = cursor.fetchall()

    columns = [column[0] for column in cursor.description] # get headers

    result = {}
    result['all_questions'] = all_questions
    result['columns'] = columns

    return result  # return questions with headers

@database_common.connection_handler 
def get_all_answers(cursor):
    cursor.execute("""SELECT * FROM answer; """) 
    all_questions = cursor.fetchall()
    return all_questions 

@database_common.connection_handler # get one questions by ID
def get_questions_by_id_dbm(cursor, q_id):

    cursor.execute("""SELECT * FROM question where id = {}; """.format(q_id))  # get question data
    question_by_id = cursor.fetchone()

    columns = [column[0] for column in cursor.description] # get headers

    result = {}
    result['question_by_id'] = question_by_id
    result['columns'] = columns

    return result  # return questions with headers


@database_common.connection_handler # get all answers connected to questions by ID
def get_answers_by_question_id_dbm(cursor, q_id):
    cursor.execute("""SELECT * FROM answer where question_id = {} order by submission_time; """.format(q_id))  # get answers data
    answers_by_question_id = cursor.fetchall()

    columns = [column[0] for column in cursor.description] # get headers

    result = {}
    result['answers_by_question_id'] = answers_by_question_id
    result['columns'] = columns

    return result  # return questions with headers





@database_common.connection_handler # moja probna funkcja
def add_new_question(cursor, title, message):
    time = util.generate_time_in_UNIX()
    submission_time = util.convert_unix_to_time_str(time)
    cursor.execute ("""
                    INSERT INTO question
                    (submission_time,view_number,vote_number,title,message)
                    VALUES('{}',0, 0, '{}', '{}');
                    """.format(submission_time,title,message))
    return cursor.rowcount


@database_common.connection_handler # add new answer and question ID
def add_new_answer_db(cursor, q_id, message):
    time = util.generate_time_in_UNIX()
    submission_time = util.convert_unix_to_time_str(time)
    cursor.execute ("""
                    INSERT INTO answer
                    (submission_time, vote_number, question_id, message)
                    VALUES('{}',0, {}, '{}');""".format(submission_time, q_id, message))
    return cursor.rowcount


@database_common.connection_handler # add new answer and question ID
def search_question_db(cursor, message):
    cursor.execute ("""SELECT DISTINCT(q.id), q.submission_time, q.view_number, q.vote_number, q.title, q.message, q.image 
                        FROM question as q join answer as a on q.id = a.question_id
                        WHERE LOWER(q.title) LIKE '%{0}%' 
                        or LOWER(q.message) like '%{0}%' 
                        or LOWER(a.message) like '%{0}%'; """.format(message))
    founded_questions = cursor.fetchall()

    columns = [column[0] for column in cursor.description]  # get headers

    result = {}
    result['founded_questions'] = founded_questions
    result['columns'] = columns

    return result  # return questions with headers


# -------------------------- DELETE QUESTION --------------------
@database_common.connection_handler # BARDZO WAZNA FUNKCJA PROSZE NIE RUSZAC
def delete_answer_db(cursor, a_id):
    cursor.execute("""DELETE FROM answer WHERE id = {};""".format(a_id))

@database_common.connection_handler # BARDZO WAZNA FUNKCJA PROSZE NIE RUSZAC
def delete_question_db(cursor, q_id):
    cursor.execute("""DELETE FROM question WHERE id = {};""".format(q_id))

@database_common.connection_handler # BARDZO WAZNA FUNKCJA PROSZE NIE RUSZAC
def delete_answer_db_by_q_id(cursor, q_id):
    cursor.execute("""DELETE FROM answer WHERE question_id = {};""".format(q_id))


# -------------------------- QUESTION VIEWS --------------------

@database_common.connection_handler
def get_question_views_db(cursor, q_id):
    cursor.execute("""select view_number FROM question WHERE id = {};""".format(q_id))
    view_number = cursor.fetchone()
    return view_number

@database_common.connection_handler
def set_question_views_db(cursor, q_id, views_number):
    cursor.execute("""UPDATE question SET view_number  = {} WHERE id = {};""".format(views_number, q_id))

