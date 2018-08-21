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

    cursor.execute("""SELECT * FROM answer where question_id = {}; """.format(q_id))  # get answers data
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




# old functions down
'''

@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""SELECT first_name, last_name FROM mentors  WHERE first_name = %(first_name)s ORDER BY first_name; """, {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_first_name_lastname(cursor):
    result = {}
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    ORDER BY first_name;
                    """)
    mentor_names = cursor.fetchall()
    # (Optional) Get a list of the column names returned from the query:
    columns = [column[0] for column in cursor.description]

    result['mentor_names'] = mentor_names
    result['columns'] = columns

    return result



@database_common.connection_handler_insert_delete  # insert
def insert_student_Markus_Schaffarzyk(cursor):
    # result = {}
    cursor.execute("""
                    INSERT INTO applicants
                    (first_name, last_name, phone_number, email, application_code)
                    VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);
                    """)
    # Markus = cursor.fetchall()
    # (Optional) Get a list of the column names returned from the query:
    # columns = [column[0] for column in cursor.description]

    # result['Markus'] = Markus
    # result['columns'] = columns

    return cursor.rowcount
'''