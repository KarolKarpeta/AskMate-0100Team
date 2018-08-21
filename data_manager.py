import database_common
import util

@database_common.connection_handler # to jest POPRAWNE ZAPYTANIE DO BAZY ASKMATE
def get_all_questions(cursor):

    cursor.execute("""SELECT * FROM question; """)  # get question data
    all_questions = cursor.fetchall()

    columns = [column[0] for column in cursor.description] # get headers

    result = {}
    result['all_questions'] = all_questions
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




# old functions down


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
