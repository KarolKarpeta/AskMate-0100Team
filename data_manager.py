import database_common
import ui_c


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""SELECT first_name, last_name FROM mentors  WHERE first_name = %(first_name)s ORDER BY first_name; """, {'first_name': first_name})
    names = cursor.fetchall()
    return names

@database_common.connection_handler # to jest POPRAWNE ZAPYTANIE DO BAZY ASKMATE
def get_all_questions(cursor):
    cursor.execute("""SELECT * FROM question; """)
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
