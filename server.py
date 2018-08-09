from flask import Flask, render_template, request, redirect, url_for
import persistence, util, logic


app = Flask(__name__)


@app.route('/list', methods=['GET', 'POST'])
def get_list():
    if request.method == 'GET':
        list_of_dict = persistence.import_from_file("sample_data/question.csv")

        list_of_dict_on_main = util.get_headers_on_main_site(list_of_dict)

        headers = persistence.import_headers("sample_data/question.csv")
        print(list_of_dict)
        print(list_of_dict_on_main)

        return render_template("q_list.html", list_of_dict_on_main=list_of_dict_on_main, headers=headers)


@app.route('/new-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        message = logic.check_message_length(request.form)
        if message == "Correct":
            return redirect("/list")
        else:
            return render_template('ask_question.html', message=message, form=request.form )
    else:
        return render_template('ask_question.html')            


@app.route('/new_questions', methods=['GET', 'POST'])
def new_question():
    if request.method == 'GET':
        return render_template("new_question.html")

    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        logic.append_row_to_csv(title, message)

        return redirect('/list')

# id,submission_time,vote_number,question_id,message,image

@app.route('/question/<q_id>', methods=['GET', 'POST'])
def question(q_id):
    list_of_dict = persistence.import_from_file("sample_data/question.csv")

    list_of_answers = persistence.import_from_file("sample_data/answer.csv")
    a_headers = persistence.import_headers("sample_data/answer.csv")
    print(a_headers)
    del a_headers[0]
    del a_headers[2]
    del a_headers[3]

    if request.method == 'GET':
        for quest in list_of_dict:
            if quest['id'] == q_id:
                return render_template("question.html", quest=quest, list_of_answers=list_of_answers, a_headers=a_headers )


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
