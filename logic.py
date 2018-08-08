import persistence

# id,submission_time,view_number,vote_number,title,message,image
# 0,1493368154,29,7,"How to make lists in Python?","I am totally new to this, any hints?",


def append_row_to_csv(title, message):
    data = [3, 1493368154, 29, 7, "title", "message", ]
    print("logic_add_question")
    persistence.export_data_to_file("sample_data/question.csv", data)
