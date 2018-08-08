import persistence
import util

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