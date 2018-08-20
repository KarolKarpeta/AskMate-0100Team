import persistence, util


def append_row_to_csv(title, message):
    data = util.prepare_list_to_save_to_the_file(title, message)
    print("logic_add_question")
    persistence.export_data_to_file("sample_data/question.csv", data)


def check_question_message_length(inputs):
    # chceck if the message length isnt shorter than 10 chars and write data to file
    new_data = {}
    if util.correct_length(inputs['message'], ">=", 10):
        new_data = {
            "title" : inputs['title'],
            "message" : inputs['message'],
            "id" : util.generate_id(),
            "submission_time" : util.generate_time_in_UNIX(),
            "view_number" : 0,
            "vote_number" :0,
            "image" : inputs.get("image")
        } 
        persistence.write_data_to_file("sample_data/question.csv", persistence.q_headers, new_data)
        return "Correct"
    else:
        return "Your message is too short. (Must be at least 10 characters long)"



def check_answer_message_length(message, q_id):
    new_data = {}
    if util.correct_length(message, ">=", 10):
        new_data = {
            "id": util.generate_id(),
            "submission_time": util.generate_time_in_UNIX(),
            "vote_number": 0,

            "question_id": q_id,

            "message": message,
            "image": "blank",
            }
        persistence.write_data_to_file("sample_data/answer.csv", persistence.a_headers, new_data)
        return "Correct"
    else:
        return "Your message is too short. (Must be at least 10 characters long)"








def get_answers_by_id(q_id):
    all_answers = persistence.import_from_file("sample_data/answer.csv")
    answers_by_id = []
    for row in all_answers:
        if row["question_id"] == q_id:
            answers_by_id.append(row)
    return answers_by_id

