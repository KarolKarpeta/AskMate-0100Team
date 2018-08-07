from flask import Flask, render_template, request, redirect, url_for
import persistence, util


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


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
