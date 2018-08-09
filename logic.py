import persistence, util

# id,submission_time,view_number,vote_number,title,message,image
# 0,1493368154,29,7,"How to make lists in Python?","I am totally new to this, any hints?",


def append_row_to_csv(title, message):
    data = util.prepare_list_to_save_to_the_file(title, message)
    print("logic_add_question")
    persistence.export_data_to_file("sample_data/question.csv", data)



def check_message_length(inputs):
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
        persistence.write_data_to_file("sample_data/question.csv", persistence.q_headers , new_data)
        return "Correct"
    else:
        return "Your message is too short. (Must be at least 10 characters long)"

