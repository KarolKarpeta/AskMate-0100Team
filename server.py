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

@app.route('/new-question', methods=['GET','POST'])
def add_question():
    if request.method == 'POST':
        message = logic.check_message_length(request.form)
        if message == "Correct":
            return redirect("/list")
        else:
            return render_template('ask_question.html', message = message, form = request.form )
    else:
        return render_template('ask_question.html')            
        



if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
