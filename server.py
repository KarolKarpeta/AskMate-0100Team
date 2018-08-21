from flask import Flask, render_template, request, redirect, url_for
import persistence, util, logic

app = Flask(__name__)


@app.route('/list', methods=['GET', 'POST'])
def get_list():
    if request.method == 'GET':
        # list_of_dict = persistence.import_from_file("sample_data/question.csv")
        # list_of_dict_on_main = util.get_headers_on_main_site(list_of_dict)
        # list_of_dict_on_main.reverse()
        # headers = persistence.import_headers("sample_data/question.csv")

        questions_and_headers = logic.get_all_questions()
        try:
            return render_template("q_list.html", list_of_dict_on_main=questions_and_headers['all_questions'], headers=questions_and_headers['columns'])
        except Exception as e:
            return render_template("500.html", error=e)



@app.route('/new-question', methods=['GET', 'POST'])
def add_question():
    msg = ""
    form_values = {}

    if request.method == 'POST':
        msg = logic.check_question_message_length(request.form)
        form_values = request.form
        if msg == "Correct":
            return redirect("/list")
    return render_template('ask_question.html', message=msg, form=form_values)


@app.route('/new_questions', methods=['GET', 'POST'])
def new_question():
    if request.method == 'GET':
        return render_template("new_question.html")

    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        logic.append_row_to_csv(title, message)

        return redirect('/list')


@app.route('/question/<q_id>', methods=['GET', 'POST'])
def question(q_id):
    print("TUTAJ")
    list_of_dict = persistence.import_from_file("sample_data/question.csv")

    answers_by_id = logic.get_answers_by_id(q_id)

    a_headers = persistence.import_headers("sample_data/answer.csv")
    del a_headers[0]
    del a_headers[2]
    del a_headers[3]

    if request.method == 'GET':
        for quest in list_of_dict:
            if quest['id'] == q_id:
                return render_template("question.html", quest=quest, answers_by_id=answers_by_id, a_headers=a_headers,
                                       message="")

    elif request.method == 'POST':
        print("kuku")
        answer_message = request.form["answer"]
        print(answer_message)

        message = logic.check_answer_message_length(answer_message, q_id)
        if str(message) == "Correct":
            print("correct")
            return redirect("/question/" + str(q_id))
        else:
            for quest in list_of_dict:
                if quest['id'] == q_id:
                    print("not correct")
                    return render_template("question.html", quest=quest, answers_by_id=answers_by_id,
                                           a_headers=a_headers, message=message)


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
