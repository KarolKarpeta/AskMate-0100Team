from flask import Flask, render_template, request, redirect, url_for
import persistence, util, logic, data_manager


app = Flask(__name__)


@app.route('/list', methods=['GET', 'POST'])  # remove methods
def get_list():
    if request.method == 'GET':

        print(data_manager.get_user_questions_answers_comments(1))
        questions_and_headers = logic.get_all_questions()

        try:
            return render_template("q_list.html", list_of_dict_on_main=questions_and_headers['all_questions'], headers=questions_and_headers['columns'])
        except Exception as e:
            return render_template("500.html", error=e)


@app.route('/new-question', methods=['GET', 'POST'])
def add_question():
    msg = ""
    form_values = {}
    all_users_name = data_manager.get_all_users()

    print("All user name", all_users_name)

    if request.method == 'POST':
        form_values = request.form
        msg = logic.check_length_message_question_db(form_values)

        if msg == "Correct":
            return redirect("/list")

    return render_template('ask_question.html', message=msg, form=form_values, all_users_name=all_users_name)


@app.route('/question/<int:q_id>', methods=['GET', 'POST'])
def question(q_id):

    q_views = logic.get_question_view_logic(q_id)
    new_views = int(q_views['view_number']) + 1

    comments_by_question_id = logic.get_comments_by_id_logic(q_id)

    logic.set_question_view_logic(q_id, new_views)

    one_question = logic.get_question_by_id_logic(q_id)
    answers_by_question_id = logic.get_answers_by_id_logic(q_id)


    return render_template("question.html", quest=one_question['question_by_id'],
                           answers_by_id=answers_by_question_id['answers_by_question_id'],
                           a_headers=answers_by_question_id['columns'],  message="", comments_by_id = comments_by_question_id['comments_by_question_id'] )


@app.route('/new_answer/<int:q_id>', methods=['GET', 'POST']) #
def new_answer(q_id):
    comments_by_question_id = logic.get_comments_by_id_logic(q_id)

    if request.method == 'POST':
        answer_message = request.form["answer"]

        one_question = logic.get_question_by_id_logic(q_id)  # ONE SQL QUERY
        answers_by_question_id = logic.get_answers_by_id_logic(q_id)

        communicate =  logic.check_answer_length_logic(answer_message) # check_answer_message_length(answer_message, q_id)

        if str(communicate) == "Correct":
            logic.add_new_answer_logic(q_id, answer_message) # insert
            answers_by_question_id = logic.get_answers_by_id_logic(q_id)
            return render_template("question.html", quest=one_question['question_by_id'],
                                   answers_by_id=answers_by_question_id['answers_by_question_id'],
                                   a_headers=answers_by_question_id['columns'], message="", comments_by_id = comments_by_question_id['comments_by_question_id'])
            #return redirect("/question/" + str(q_id))
        else:
            return render_template("question.html", quest=one_question['question_by_id'],
                                           answers_by_id=answers_by_question_id['answers_by_question_id'],
                                           a_headers=answers_by_question_id['columns'], message=communicate, comments_by_id = comments_by_question_id['comments_by_question_id'])



@app.route('/search', methods=['GET', 'POST'])
def search_question():
    founded_question = {}

    if request.method == 'POST':

        search_massage = request.form['search_message']
        print(search_massage)
        founded_question = logic.search_question_logic(search_massage.lower())
        print(founded_question)
    try:
        return render_template("q_list.html", list_of_dict_on_main = founded_question['founded_questions'],
                               headers=founded_question['columns'])
    except Exception as e:
        return render_template("500.html", error=e)



@app.route('/new-comment/<int:q_id>', methods=['POST'])
def comment(q_id):

    # one_question = logic.get_question_by_id_logic(q_id)


    comment_message = request.form["comment"]
    logic.add_new_comment_logic(q_id, comment_message)
    return redirect("/question/" + str(q_id))


@app.route('/question/<int:q_id>/delete', methods=['GET', 'POST'])
def delete_question(q_id):
    if request.method == 'POST': # TUTAJ USUNELAM QUESTION BO NIE POT
        answer = logic.get_all_answers()
        for dic in answer:
            if dic['question_id'] == q_id:
                logic.delete_answer_logic_by_q_id(q_id)
                
        logic.delete_question_logic(q_id)
    try:
        return redirect("/list")
    except Exception as e:
        return render_template("500.html", error=e)


@app.route('/answer/<int:a_id>/delete', methods=['GET', 'POST'])
def delete_answer(a_id):
    if request.method == 'POST':
        answers = logic.get_all_answers() # CO TO JEST BASIU ??????????????????????? MOJ PRZYCIEMNIONY UMYSL, JUZ ZMIENILAM
        for dic in answers:
            if dic['id'] == a_id:
                q_id = dic['question_id']

        logic.delete_answer_logic(a_id)
    try:
        return redirect("/question/" + str(q_id))
    except Exception as e:
        return render_template("500.html", error=e)


@app.route('/register', methods=['GET', 'POST'])
def register():
    mess = ""

    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mess = logic.check_if_user_exists(username, password)

    if mess == "USER SUCCESSFULLY ADDED":
        return redirect("/list")
    else:
        return render_template('register.html', username=username, message=mess)

@app.route('/users')
def users_table():
    try:
        users = logic.check_if_database_works_and_has_users()
        return render_template('users.html', users=users)

    except Exception as e:
        return render_template("500.html", error=e)


@app.route('/user_page/<int:user_id>')
def user_page(user_id):
    try:

        list_of_lists = logic.get_users_questions_answers_comments_by_id(user_id)
        print("list of list", list_of_lists)

        print("q", list_of_lists[0])
        print("a", list_of_lists[1])
        print("c", list_of_lists[2])


        return render_template('user_menu.html', list_of_questions = list_of_lists[0], list_of_answers = list_of_lists[1], list_of_comments = list_of_lists[2], user_id = user_id )

    except Exception as e:
        return render_template("500.html", error=e)




if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
