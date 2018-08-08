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


@app.route('/new_question', methods=['GET', 'POST'])
def new_question():
    if request.method == 'GET':
        return render_template("new_question.html")

    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']
        logic.append_row_to_csv(title, message)

        return redirect('/list')





if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
