from flask import Flask, render_template, request, redirect, url_for
import persistence, util, logic

app = Flask(__name__)


@app.route('/list', methods=['GET', 'POST'])
def get_list():
    if request.method == 'GET':

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
        msg = logic.check_length_message_question_db(request.form)
        form_values = request.form
        if msg == "Correct":
            return redirect("/list")
    return render_template('ask_question.html', message=msg, form=form_values)



@app.route('/question/<int:q_id>', methods=['GET', 'POST'])
def question(q_id):

    one_question = logic.get_question_by_id_logic(q_id)
    answers_by_question_id = logic.get_answers_by_id_logic(q_id)
    comments_by_question_id = logic.get_comments_by_id_logic(q_id)

    if request.method == 'GET':
        return render_template("question.html", quest=one_question['question_by_id'], answers_by_id=answers_by_question_id['answers_by_question_id'], comments_by_id=comments_by_question_id['comments_by_question_id'], a_headers=answers_by_question_id['columns'],  message="")

    elif request.method == 'POST':

            answer_message = request.form["answer"]
            communicate = logic.check_answer_length_logic(answer_message) # check_answer_message_length(answer_message, q_id)

            if str(communicate) == "Correct":
                logic.add_new_answer_logic(q_id, answer_message) # insert
                return redirect("/question/" + str(q_id))
            else:
                return render_template("question.html", quest=one_question['question_by_id'],
                                           answers_by_id=answers_by_question_id['answers_by_question_id'],
                                           a_headers=answers_by_question_id['columns'], message=communicate)

@app.route('/search', methods=['GET', 'POST'])
def search_question():
    founded_question = {}

    if request.method == 'POST':

        search_massage = request.form['search_message']
        print(search_massage)
        founded_question = logic.search_question_logic(search_massage.lower())
        print(founded_question)
    try:
        return render_template("q_list.html", list_of_dict_on_main = founded_question['founded_questions'], headers=founded_question['columns'])
    except Exception as e:
        return render_template("500.html", error=e)



@app.route('/new-comment/<int:q_id>', methods=['POST'])
def comment(q_id):

    one_question = logic.get_question_by_id_logic(q_id)
    comments_by_question_id = logic.get_comments_by_id_logic(q_id)

    comment_message = request.form["comment"]
    logic.add_new_comment_logic(q_id, comment_message)
    #  return redirect('/question/<int:q_id>')
    return redirect("/question/" + str(q_id))

# id,submission_time,vote_number,question_id,message,image


'''
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
                return render_template("question.html", quest=quest, answers_by_id=answers_by_id, a_headers=a_headers, message="")

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
                                           
                                           
                                           
                        {% for key, value in row.items() %} from question.html TO DELETE !!!!!!!!!!!
                            {% if key in a_headers %}
                                <td>{{ value }}</td>
                            {% endif %}
                        {% endfor %}
'''

if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True
    )
